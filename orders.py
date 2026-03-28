import logging
from bot.client import get_client

def place_order(symbol, side, order_type, quantity, price=None):
    client = get_client()

    try:
        if order_type == "MARKET":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )

        elif order_type == "LIMIT":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )

        logging.info(f"Order Response: {order}")
        return order

    except Exception as e:
        logging.error(f"Error placing order: {str(e)}")
        raise