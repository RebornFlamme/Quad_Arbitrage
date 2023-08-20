import ccxt.async_support as ccxt
import asyncio
from get_pairs import get_pairs

# Replace with your list of trading pairs
pairs = ['ETH/BTC', 'LTC/BTC', 'BNB/BTC', 'NEO/BTC', 'QTUM/ETH', 'EOS/ETH', 'SNT/ETH', 'BNT/ETH', 'BCC/BTC', 'GAS/BTC', 'BNB/ETH', 'BTC/USDT', 'ETH/USDT', 'HSR/BTC', 'OAX/ETH', 'DNT/ETH', 'MCO/ETH', 'ICN/ETH', 'MCO/BTC', 'WTC/BTC', 'WTC/ETH', 'LRC/BTC', 'LRC/ETH', 'QTUM/BTC', 'YOYOW/BTC', 'OMG/BTC', 'OMG/ETH', 'ZRX/BTC', 'ZRX/ETH', 'STRAT/BTC', 'STRAT/ETH', 'SNGLS/BTC', 'SNGLS/ETH', 'BQX/BTC', 'BQX/ETH', 'KNC/BTC', 'KNC/ETH', 'FUN/BTC', 'FUN/ETH', 'SNM/BTC', 'SNM/ETH', 'NEO/ETH', 'IOTA/BTC', 'IOTA/ETH', 'LINK/BTC', 'LINK/ETH', 'XVG/BTC', 'XVG/ETH', 'SALT/BTC', 'SALT/ETH', 'MDA/BTC', 'MDA/ETH', 'MTL/BTC', 'MTL/ETH', 'SUB/BTC', 'SUB/ETH', 'EOS/BTC', 'SNT/BTC', 'ETC/ETH', 'ETC/BTC', 'MTH/BTC', 'MTH/ETH', 'ENG/BTC', 'ENG/ETH', 'DNT/BTC', 'ZEC/BTC', 'ZEC/ETH', 'BNT/BTC', 'AST/BTC', 'AST/ETH', 'DASH/BTC', 'DASH/ETH', 'OAX/BTC', 'ICN/BTC', 'BTG/BTC', 'BTG/ETH', 'EVX/BTC', 'EVX/ETH', 'REQ/BTC', 'REQ/ETH', 'VIB/BTC', 'VIB/ETH', 'HSR/ETH', 'TRX/BTC', 'TRX/ETH', 'POWR/BTC', 'POWR/ETH', 'ARK/BTC', 'ARK/ETH', 'YOYOW/ETH', 'XRP/BTC', 'XRP/ETH', 'MOD/BTC', 'MOD/ETH', 'ENJ/BTC', 'ENJ/ETH', 'STORJ/BTC', 'STORJ/ETH', 'BNB/USDT', 'VEN/BNB', 'YOYOW/BNB', 'POWR/BNB', 'VEN/BTC', 'VEN/ETH', 'KMD/BTC', 'KMD/ETH', 'NULS/BNB', 'RCN/BTC', 'RCN/ETH', 'RCN/BNB', 'NULS/BTC', 'NULS/ETH', 'RDN/BTC', 'RDN/ETH', 'RDN/BNB', 'XMR/BTC', 'XMR/ETH', 'DLT/BNB', 'WTC/BNB', 'DLT/BTC', 'DLT/ETH', 'AMB/BTC', 'AMB/ETH', 'AMB/BNB', 'BCC/ETH', 'BCC/USDT', 'BCC/BNB', 'BAT/BTC', 'BAT/ETH', 'BAT/BNB', 'BCPT/BTC', 'BCPT/ETH', 'BCPT/BNB', 'ARN/BTC', 'ARN/ETH', 'GVT/BTC', 'GVT/ETH', 'CDT/BTC', 'CDT/ETH', 'GXS/BTC', 'GXS/ETH', 'NEO/USDT', 'NEO/BNB', 'POE/BTC', 'POE/ETH', 'QSP/BTC', 'QSP/ETH', 'QSP/BNB', 'BTS/BTC', 'BTS/ETH', 'BTS/BNB', 'XZC/BTC', 'XZC/ETH', 'XZC/BNB', 'LSK/BTC', 'LSK/ETH', 'LSK/BNB', 'TNT/BTC', 'TNT/ETH', 'FUEL/BTC', 'FUEL/ETH', 'MANA/BTC', 'MANA/ETH', 'BCD/BTC', 'BCD/ETH', 'DGD/BTC', 'DGD/ETH', 'IOTA/BNB', 'ADX/BTC', 'ADX/ETH', 'ADX/BNB', 'ADA/BTC', 'ADA/ETH', 'PPT/BTC', 'PPT/ETH', 'CMT/BTC', 'CMT/ETH', 'CMT/BNB', 'XLM/BTC', 'XLM/ETH', 'XLM/BNB', 'CND/BTC', 'CND/ETH', 'CND/BNB', 'LEND/BTC', 'LEND/ETH', 'WABI/BTC', 'WABI/ETH', 'WABI/BNB', 'LTC/ETH', 'LTC/USDT', 'LTC/BNB', 'TNB/BTC', 'TNB/ETH', 'WAVES/BTC', 'WAVES/ETH', 'WAVES/BNB', 'GTO/BTC', 'GTO/ETH', 'GTO/BNB', 'ICX/BTC', 'ICX/ETH', 'ICX/BNB', 'OST/BTC', 'OST/ETH', 'OST/BNB', 'ELF/BTC', 'ELF/ETH', 'AION/BTC', 'AION/ETH', 'AION/BNB', 'NEBL/BTC', 'NEBL/BNB', 'BRD/BTC', 'BRD/ETH', 'BRD/BNB', 'MCO/BNB', 'EDO/BTC', 'EDO/ETH', 'WINGS/BTC', 'WINGS/ETH', 'NAV/BTC', 'NAV/ETH', 'NAV/BNB', 'LUN/BTC', 'LUN/ETH', 'TRIG/BTC', 'TRIG/ETH', 'TRIG/BNB', 'APPC/BTC', 'APPC/ETH', 'APPC/BNB', 'VIBE/BTC', 'VIBE/ETH', 'RLC/BTC', 'RLC/ETH', 'RLC/BNB', 'INS/BTC', 'INS/ETH', 'PIVX/BTC', 'PIVX/BNB', 'IOST/BTC', 'IOST/ETH', 'CHAT/BTC', 'CHAT/ETH', 'STEEM/BTC', 'STEEM/ETH', 'STEEM/BNB', 'NANO/BTC', 'NANO/ETH', 'NANO/BNB', 'VIA/BTC', 'VIA/ETH', 'VIA/BNB', 'BLZ/BTC', 'BLZ/ETH', 'BLZ/BNB', 'AE/BTC', 'AE/ETH', 'AE/BNB', 'RPX/BTC', 'RPX/ETH', 'RPX/BNB', 'NCASH/BTC', 'NCASH/ETH', 'NCASH/BNB', 'POA/BTC', 'POA/ETH', 'POA/BNB', 'ZIL/BTC', 'ZIL/ETH', 'ZIL/BNB', 'ONT/BTC', 'ONT/ETH', 'ONT/BNB', 'STORM/BTC', 'STORM/ETH', 'STORM/BNB', 'QTUM/BNB', 'QTUM/USDT', 'XEM/BTC', 'XEM/ETH', 'XEM/BNB', 'WAN/BTC', 'WAN/ETH', 'WAN/BNB', 'WPR/BTC', 'WPR/ETH', 'QLC/BTC', 'QLC/ETH', 'SYS/BTC', 'SYS/ETH', 'SYS/BNB', 'QLC/BNB', 'GRS/BTC', 'GRS/ETH', 'ADA/USDT', 'ADA/BNB', 'CLOAK/BTC', 'CLOAK/ETH', 'GNT/BTC', 'GNT/ETH', 'GNT/BNB', 'LOOM/BTC', 'LOOM/ETH', 'LOOM/BNB', 'XRP/USDT', 'BCN/BTC', 'BCN/ETH', 'BCN/BNB', 'REP/BTC', 'REP/BNB', 'TUSD/BTC', 'TUSD/ETH', 'TUSD/BNB', 'ZEN/BTC', 'ZEN/ETH', 'ZEN/BNB', 'SKY/BTC', 'SKY/ETH', 'SKY/BNB', 'EOS/USDT', 'EOS/BNB', 'CVC/BTC', 'CVC/ETH', 'CVC/BNB', 'THETA/BTC', 'THETA/ETH', 'THETA/BNB', 'XRP/BNB', 'TUSD/USDT', 'IOTA/USDT', 'XLM/USDT', 'IOTX/BTC', 'IOTX/ETH', 'QKC/BTC', 'QKC/ETH', 'AGI/BTC', 'AGI/ETH', 'AGI/BNB', 'NXS/BTC', 'NXS/ETH', 'NXS/BNB', 'ENJ/BNB', 'DATA/BTC', 'DATA/ETH', 'ONT/USDT', 'TRX/BNB', 'TRX/USDT', 'ETC/USDT', 'ETC/BNB', 'ICX/USDT', 'SC/BTC', 'SC/ETH', 'NPXS/BTC', 'NPXS/ETH', 'VEN/USDT', 'KEY/BTC', 'KEY/ETH', 'NAS/BTC', 'NAS/ETH', 'NAS/BNB', 'MFT/BTC', 'MFT/ETH', 'MFT/BNB', 'DENT/BTC', 'DENT/ETH', 'ARDR/BTC', 'ARDR/ETH', 'ARDR/BNB', 'NULS/USDT', 'HOT/BTC', 'HOT/ETH', 'VET/BTC', 'VET/ETH', 'VET/USDT', 'VET/BNB', 'DOCK/BTC', 'DOCK/ETH', 'POLY/BTC', 'POLY/BNB', 'PHX/BTC', 'PHX/ETH', 'PHX/BNB', 'HC/BTC', 'HC/ETH', 'GO/BTC', 'GO/BNB', 'PAX/BTC', 'PAX/BNB', 'PAX/USDT', 'PAX/ETH', 'RVN/BTC', 'DCR/BTC', 'DCR/BNB', 'USDC/BNB', 'MITH/BTC', 'MITH/BNB', 'BCH/BTC', 'BSV/BTC', 'BCH/USDT', 'BSV/USDT', 'BNB/PAX', 'BTC/PAX', 'ETH/PAX', 'XRP/PAX', 'EOS/PAX', 'XLM/PAX', 'REN/BTC', 'REN/BNB', 'BNB/USDC', 'BTC/USDC', 'ETH/USDC', 'XRP/USDC', 'EOS/USDC', 'XLM/USDC', 'USDC/USDT', 'TRX/XRP', 'XZC/XRP', 'USDC/PAX', 'LINK/USDT', 'LINK/PAX', 'LINK/USDC', 'WAVES/USDT', 'WAVES/PAX', 'WAVES/USDC', 'BCH/PAX', 'BCH/USDC', 'BSV/PAX', 'BSV/USDC', 'LTC/PAX', 'LTC/USDC', 'TRX/PAX', 'TRX/USDC', 'BTT/BTC', 'BTT/BNB', 'BTT/USDT', 'BNB/USDS', 'BTC/USDS', 'USDS/USDT', 'USDS/PAX', 'USDS/USDC', 'BTT/PAX', 'BTT/USDC', 'ONG/BNB', 'ONG/BTC', 'ONG/USDT', 'HOT/BNB', 'HOT/USDT', 'ZIL/USDT', 'ZRX/BNB', 'ZRX/USDT', 'FET/BNB', 'FET/BTC', 'FET/USDT', 'BAT/USDT', 'XMR/BNB', 'XMR/USDT', 'ZEC/BNB', 'ZEC/USDT', 'ZEC/PAX', 'ZEC/USDC', 'IOST/USDT', 'CELR/BNB', 'CELR/BTC', 'CELR/USDT', 'ADA/PAX', 'ADA/USDC', 'NEO/PAX', 'NEO/USDC', 'DASH/BNB', 'DASH/USDT', 'NANO/USDT', 'OMG/BNB', 'OMG/USDT', 'THETA/USDT', 'ENJ/USDT', 'MITH/USDT', 'MATIC/BNB', 'MATIC/BTC', 'MATIC/USDT', 'ATOM/BNB', 'ATOM/BTC', 'ATOM/USDT', 'ATOM/USDC', 'ATOM/PAX', 'ETC/USDC', 'ETC/PAX', 'BAT/USDC', 'BAT/PAX', 'PHB/BNB', 'PHB/BTC', 'PHB/USDC', 'PHB/PAX', 'TFUEL/BNB', 'TFUEL/BTC', 'TFUEL/USDT', 'TFUEL/USDC', 'TFUEL/PAX', 'ONE/BNB']
# Replace with the exchange name you're using
exchange_name = 'kucoin'  # Example: 'binance'
coin_dict = {}

async def fetch_prices(pair, exchange):
    try : 
        ticker = await exchange.fetch_ticker(pair)
        bid_price = ticker['bid']
        ask_price = ticker['ask']
    except:
        print(f'Error while fetching price of {pair}')
    return pair, bid_price, ask_price


async def main():
    exchange = getattr(ccxt, exchange_name)()
    tasks = [fetch_prices(pair, exchange) for pair in pairs]
    results = await asyncio.gather(*tasks)
    
    for pair, bid_price, ask_price in results:
        #coin_dict[f'{pair}'] = {}
        #coin_dict[f'{pair}']['Bid'] = bid_price
        #coin_dict[f'{pair}']['Ask'] = ask_price

        print(f"Pair: {pair}, Bid Price: {bid_price}, Ask Price: {ask_price}")
    
    await exchange.close()



if __name__ == '__main__':
    
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

    print("Hello")