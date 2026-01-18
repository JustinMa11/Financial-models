#多功能计算器（后续功能开发中……）
while True:
    choice = input("请选择功能,输入数字即可：\n1.CAPM\n2.债券现值\n3.期货保证金与杠杆率计算（多头）\n4.退出\n")
    if choice == '1':
        # CAPM计算
        risk_free_rate = float(input("请输入无风险利率（%）：")) / 100
        beta = float(input("请输入股票的Beta值："))
        market_return = float(input("请输入市场预期收益率（%）：")) / 100
        expected_return = risk_free_rate + beta * (market_return - risk_free_rate)
        print(f"股票的预期收益率为：{expected_return * 100:.2f}%")
        answer = input("是否需要继续计算？(yes/no): ")
        if answer == 'no':
            break
        elif answer == 'yes':
            continue
    elif choice == '2':
        # 债券现值计算
        face_value = float(input("请输入债券面值："))
        coupon_rate = float(input("请输入票面利率（%）：")) / 100
        years_to_maturity = int(input("请输入到期年限："))
        market_rate = float(input("请输入市场利率（%）：")) / 100
        year_coupon_payment = face_value * coupon_rate
        present_value_coupons = sum([year_coupon_payment / (1 + market_rate) ** t for t in range(1, years_to_maturity + 1)])
        present_value_face = face_value / (1 + market_rate) ** years_to_maturity
        bond_price = present_value_coupons + present_value_face
        print(f"债券的现值为：{bond_price:.2f}")
        answer = input("是否需要继续计算？(yes/no): ")
        if answer == 'no':
            break
        elif answer == 'yes':
            continue
    elif choice == '3':
        # 期货保证金与杠杆率计算（目前只适用于多头）
        entry_price = float(input("请输入每单位价格: "))
        contracts = int(input("请输入手数: "))
        contract_size = float(input("请输入合约乘数: "))
        margin_rate = float(input("请输入保证金率（小数）"))
        margin = entry_price * contracts * contract_size * margin_rate
        leverage_ratio = 1 / margin_rate
        total_capital = float(input("请输入总资金: "))
        rate = margin / total_capital
        #(初始价格-被迫平仓价格)*合约乘数*手数=总资金-开仓保证金
        liquidation_price = (margin - total_capital)/ (contracts * contract_size) + entry_price
        print(f"强制平仓价格为：{liquidation_price:.2f}")
        print(f"资金使用率为：{rate:.2%}")
        if rate > 0.7:
            print("警告：资金使用率过高，风险较大！")    
        print(f"期货合约的杠杆率为：{leverage_ratio:.2f}倍")
        print(f"所需保证金为：{margin:.2f}")
        answer = input("是否需要继续计算？(yes/no): ")
        if answer == 'no':
            break
        elif answer == 'yes':
            continue        
    elif choice == '4':
        print("退出计算器。\n\t感谢使用！")
        break
    else:
        print("无效选择，请重新输入。")
        break