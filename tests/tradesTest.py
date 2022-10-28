from .. import pywaves as pw

def test_tradesLimit():
    WAVES_BTC = pw.AssetPair(pw.WAVES, pw.BTC)
    trades = WAVES_BTC.trades(10)

    assert len(trades) > 0

def test_tradesTimestamp():
    WAVES_BTC = pw.AssetPair(pw.WAVES, pw.BTC)
    trades = WAVES_BTC.trades(1666743707000, 1666843707000)

    print(trades)
