def total_cal(bill_amount,tip_perc):
    total=bill_amount*(1+0.01*tip_perc)
    print(f"Please pay ${total}")
total_cal(5,20)