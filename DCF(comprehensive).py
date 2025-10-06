# FCFE--股权自由现金流折现模型 - 不保存文件，只进行计算和显示
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'DejaVu Sans']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
print("=== 详细版DCF估值分析 ===")

# 基础参数
company_name = input("请输入公司名称: ")
net_income = float(input("请输入当前年度净利润 (百万美元): "))
depreciation = float(input("请输入当前年度折旧、摊销 (百万美元): "))
operating_working_capital = float(input("请输入当前年度营运资本增加 (百万美元): "))
capital_expenditures = float(input("请输入当前年度资本支出 (百万美元): "))
long_term_operating_debt = float(input("请输入当前年度长期经营性债务增加 (百万美元): "))
long_term_operating_assets = float(input("请输入当前年度长期营运资产增加 (百万美元): "))
interest_bearing_debt = float(input("请输入当前年度有息负债增加 (百万美元): "))
repayment_of_debt = float(input("请输入当前年度债务本金偿还 (百万美元): "))
FCFE = net_income + depreciation - operating_working_capital - capital_expenditures + long_term_operating_debt - long_term_operating_assets + interest_bearing_debt - repayment_of_debt
#current_ebitda = float(input("请输入当前年度EBITDA (百万美元): "))
#M = float(input("请输入五年后预期退出倍数: "))
#提供另一种终值算法——EBITDA&退出倍数
#M和EBITDA决定了终值
forecast_years = 5 #详细预测期——五年
print(f"您选择的公司是: {company_name},详细预测期为{forecast_years}年")
#wacc= Rf + Beta * (Rm - Rf), 可由CAPM模型自行计算
wacc = float(input("请输入加权平均资本成本WACC (百分比): ")) / 100
growth_rate = float(input("请输入现金流长期增长率 (百分比): ")) / 100
if growth_rate >= wacc:
    print("警告: 长期增长率应低于WACC，否则估值无意义!请采用EBITDA&退出倍数计算终值")
net_debt = float(input("请输入净债务 (百万美元): "))  # 净债务 = 总债务 - 现金
# 生成预测数据
years = list(range(2025, 2025 + forecast_years))
#获取预期增长率
while True:
#创建重复循环，直到得到符合格式的数据
    try:
        growth_input = input("请输入未来五年详细预期股权自由现金流增长率: ").strip()
        # 分割输入并转换为浮点数
        revenue_growth = [float(x) for x in growth_input.split()]
        
        # 验证输入
        if len(revenue_growth) != 5:
            print("错误：请输入恰好5个数值")
            continue
            
        # 验证数值范围（假设增长率在-100%到+100%之间是合理的）
        if any(g < -1.0 or g > 1.0 for g in revenue_growth):
            print("错误：增长率应在-1.0到1.0之间（-100%到+100%）")
            continue
            
        print(f"您输入的增长率: {[f'{g*100:.1f}%' for g in revenue_growth]}")
        break
        
    except ValueError:
        print("错误：请输入有效的数字，用空格分隔")
    except Exception as e:
        print(f"输入错误: {e}")

# 计算自由现金流 (简化计算)
fcf_list = []
current_fcf = FCFE  # 假设FCF利润率为输入值RATE

for i, year in enumerate(years):
    fcf = current_fcf * (1 + revenue_growth[i])
    fcf_list.append(fcf)
    current_fcf = fcf

# 创建DataFrame
df = pd.DataFrame({
    'Year': years,
    'Revenue_Growth': revenue_growth,
    'FCF': fcf_list
})

# 计算现值
df['PV_FCF'] = df['FCF'] / ((1 + wacc) ** (df['Year'] - 2024))

# 计算终值 TV = FCF_n * (1 + g) / (WACC - g)
terminal_value = fcf_list[-1] * (1 + growth_rate) / (wacc - growth_rate)
pv_terminal = terminal_value /( (1 + wacc) ** forecast_years)

# 计算总价值
equity_amount = float(input("请输入总股本 (百万股): "))  # 总股本
equity_value = df['PV_FCF'].sum() + pv_terminal
enterprise_value = equity_value + net_debt  # 减去净债务
value_per_share = equity_value / equity_amount    # 除以总股本

print("\n财务预测:")
print(df.round(2))

print(f"\n估值结果:")
print(f"企业价值: ${enterprise_value:,.2f}M")
print(f"股权价值: ${equity_value:,.2f}M")
print(f"每股价值: ${value_per_share:.2f}")

# 简单可视化
plt.figure(figsize=(10, 6))
plt.subplot(1, 2, 1)
plt.bar(df['Year'], df['FCF'], color='lightblue')
plt.title('自由现金流预测')
plt.ylabel('FCF ($M)')

plt.subplot(1, 2, 2)
components = [df['PV_FCF'].sum(), pv_terminal]
labels = ['预测期现金流', '终值']
plt.pie(components, labels=labels, autopct='%1.1f%%')
plt.title('components of valuation')

plt.tight_layout()
plt.show()

print("\n分析完成! ")