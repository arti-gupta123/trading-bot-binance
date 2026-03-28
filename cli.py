print("Program started")  # DEBUG

import argparse
from bot.orders import place_order
from bot.validators import validate_order
from bot.logging_config import setup_logger

setup_logger()

def main():
    print("Inside main function")  # DEBUG

    parser = argparse.ArgumentParser()

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    try:
        print("\n--- Order Summary ---")
        print(vars(args))  # DEBUG

        validate_order(
            args.symbol,
            args.side,
            args.type,
            args.quantity,
            args.price
        )

        print("Validation successful")  # DEBUG

        order = place_order(
            args.symbol,
            args.side,
            args.type,
            args.quantity,
            args.price
        )

        print("\n--- Order Response ---")
        print(f"Order ID: {order.get('orderId')}")
        print(f"Status: {order.get('status')}")
        print(f"Executed Qty: {order.get('executedQty')}")

        print("\nOrder placed successfully")

    except Exception as e:
        print(f"\nError: {str(e)}")

if __name__ == "__main__":
    main()