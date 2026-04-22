import argparse
from bot.client import get_client
from bot.orders import place_order
from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price
)
from bot.logging_config import setup_logging


def main():
    setup_logging()

    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")

    parser.add_argument("--symbol", required=True, help="Trading pair (e.g., BTCUSDT)")
    parser.add_argument("--side", required=True, help="BUY or SELL")
    parser.add_argument("--type", required=True, help="MARKET or LIMIT")
    parser.add_argument("--quantity", required=True, type=float, help="Order quantity")
    parser.add_argument("--price", type=float, help="Price (required for LIMIT)")

    args = parser.parse_args()

    try:
        # Validate inputs
        validate_side(args.side)
        validate_order_type(args.type)
        validate_quantity(args.quantity)
        validate_price(args.type, args.price)

        client = get_client()

        print("\n📌 Order Request Summary:")
        print(vars(args))

        order = place_order(
            client=client,
            symbol=args.symbol,
            side=args.side,
            order_type=args.type,
            quantity=args.quantity,
            price=args.price
        )

        print("\n✅ Order Placed Successfully!")
        print({
            "orderId": order.get("orderId"),
            "status": order.get("status"),
            "executedQty": order.get("executedQty"),
            "avgPrice": order.get("avgPrice", "N/A")
        })

    except Exception as e:
        print(f"\n❌ Error: {str(e)}")


if __name__ == "__main__":
    main()
