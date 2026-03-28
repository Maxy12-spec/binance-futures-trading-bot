import argparse
from bot.validators import validate_order
from bot.orders import place_market_order, place_limit_order
from bot.logging_config import setup_logger

setup_logger()

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--qty", type=float, required=True)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    try:
        validate_order(args.symbol, args.side, args.type, args.qty, args.price)

        print("\nOrder Summary:")
        print(args)

        if args.type == "MARKET":
            result = place_market_order(args.symbol, args.side, args.qty)
        else:
            result = place_limit_order(args.symbol, args.side, args.qty, args.price)

        print("\nOrder Response:")
        print(result)

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()