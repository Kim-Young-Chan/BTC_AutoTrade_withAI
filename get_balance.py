import pyupbit

access = "rSraQEz3RysLaOYUQxlhdFSKLqTMq0oMgkVotimF"          # 본인 값으로 변경
secret = "1WFsbostIGlWAkFCexuiHHkgJYOxW5HcJjesqxTp"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-BTC"))     # KRW-BTC 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회