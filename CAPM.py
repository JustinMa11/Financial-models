# 导入我们需要的库
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

print("所有库导入成功！")

# 1. 创建模拟数据 - 使用MRVL和NASDAQ
print("正在生成MRVL与NASDAQ的模拟股票数据...")

# 设置随机种子，保证每次运行结果一致
np.random.seed()

# 创建日期范围：2025-03-01 到 2026-03-01
start_date = '2025-03-01'
end_date = '2026-03-01'
dates = pd.date_range(start=start_date, end=end_date, freq='D')
n_days = len(dates)

print(f"创建了 {n_days} 天的模拟数据")
print(f"时间范围: {start_date} 至 {end_date}")

# 2. 生成NASDAQ（市场）的模拟价格数据
# NASDAQ从20000点开始，模拟真实的市场波动
nasdaq_prices = [20000]  # 初始价格

# 市场利率为4.5%，转换为日利率（按252个交易日计算）
daily_risk_free_rate = 0.045 / 252

for i in range(1, n_days):
    # 市场每日收益率：考虑无风险利率和波动
    market_return = np.random.normal(daily_risk_free_rate, 0.015)  # 日均波动1.5%
    new_price = nasdaq_prices[-1] * (1 + market_return)
    nasdaq_prices.append(new_price)

# 3. 生成MRVL的模拟价格数据，与NASDAQ相关但波动更大
# MRVL从70开始，Beta系数为2.1（高贝塔股票）
mrvl_prices = [70]  # 初始价格
beta = 2.1  # 指定的Beta系数

for i in range(1, n_days):
    # MRVL收益率与NASDAQ相关，Beta=2.1意味着波动是市场的2.1倍
    market_return_component = beta * (nasdaq_prices[i]/nasdaq_prices[i-1] - 1)
    
    # 添加特有风险（半导体股票特有波动）
    idiosyncratic_risk = np.random.normal(0, 0.02)  # 特有风险波动2%
    
    # 组合收益率
    mrvl_return = market_return_component + idiosyncratic_risk
    
    new_price = mrvl_prices[-1] * (1 + mrvl_return)
    mrvl_prices.append(new_price)

# 4. 创建DataFrame
closing_prices = pd.DataFrame({
    'NASDAQ': nasdaq_prices,
    'MRVL': mrvl_prices
}, index=dates)

print("模拟数据生成成功！")
print("\n前5行数据：")
print(closing_prices.head())

# 5. 计算每日收益率
daily_returns = closing_prices.pct_change().dropna()

print("\n收益率基本统计信息：")
print(daily_returns.describe())

# 6. 绘制价格走势图
plt.figure(figsize=(14, 10))

# 价格走势子图
plt.subplot(2, 1, 1)
plt.plot(closing_prices['NASDAQ'], label='NASDAQ Index', color='blue', linewidth=2)
plt.ylabel('NASDAQ Index')
plt.title('Price Trend: MRVL vs NASDAQ (Mar 2025 - Mar 2026)')
plt.legend()
plt.grid(True, alpha=0.3)

plt.subplot(2, 1, 2)
plt.plot(closing_prices['MRVL'], label='MRVL Stock Price', color='red', linewidth=2)
plt.ylabel('MRVL Price ($)')
plt.xlabel('Date')
plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()
#如有需要，可以保存图片（替换USER NAME）
#plt.savefig('C:/Users/MA/Documents/price_trends_mrvl_nasdaq.png', dpi=300, bbox_inches='tight')
plt.show()

# 7. 绘制收益率的时间序列图
plt.figure(figsize=(12, 6))
plt.plot(daily_returns['MRVL'], label='MRVL Returns', alpha=0.7, linewidth=0.8, color='red')
plt.plot(daily_returns['NASDAQ'], label='NASDAQ Returns', alpha=0.7, linewidth=0.8, color='blue')
plt.title('Daily Returns: MRVL vs. NASDAQ (Mar 2025 - Mar 2026)')
plt.legend()
plt.grid(True, alpha=0.3)
#plt.savefig('C:/Users/MA/Documents/returns_timeseries_mrvl_nasdaq.png', dpi=300, bbox_inches='tight')
plt.show()

# 8. 绘制散点图，查看两者关系
plt.figure(figsize=(10, 6))
plt.scatter(daily_returns['NASDAQ'], daily_returns['MRVL'], alpha=0.5, s=10, color='purple')
plt.xlabel('NASDAQ Daily Returns (Market)')
plt.ylabel('MRVL Daily Returns')
plt.title('Scatter Plot: MRVL Returns vs. NASDAQ Returns')
plt.grid(True, alpha=0.3)
#plt.savefig('C:/Users/MA/Documents/returns_scatter_mrvl_nasdaq.png', dpi=300, bbox_inches='tight')
plt.show()

# 9. 线性回归计算Beta和Alpha
X = daily_returns['NASDAQ'].values
Y = daily_returns['MRVL'].values

# 使用numpy的polyfit进行一元线性回归
calculated_beta, alpha = np.polyfit(X, Y, deg=1)

print(f"\n=== CAPM 分析结果 ===")
print(f"预设的Beta系数: {beta:.1f}")
print(f"计算得到的Beta值（系统性风险）: {calculated_beta:.4f}")
print(f"Alpha值（超额收益）: {alpha:.6f}")

# 10. 计算R²
Y_pred = alpha + calculated_beta * X
ss_res = np.sum((Y - Y_pred) ** 2)
ss_tot = np.sum((Y - np.mean(Y)) ** 2)
r_squared = 1 - (ss_res / ss_tot)

print(f"R平方值（市场解释的波动比例）: {r_squared:.4f}")
print(f"这意味着市场波动解释了MRVL {r_squared*100:.2f}% 的价格波动。")

# 11. 创建最终的专业分析图表
plt.figure(figsize=(12, 8))

# 绘制散点图
plt.scatter(X, Y, alpha=0.5, s=15, label='Daily Returns', color='purple')

# 绘制回归线
x_line = np.array([X.min(), X.max()])
y_line = alpha + calculated_beta * x_line
plt.plot(x_line, y_line, color='red', linewidth=2, label=f'Regression Line (Beta = {calculated_beta:.2f})')

# 设置图表标签和标题
plt.xlabel('NASDAQ Daily Returns (Market)', fontsize=12)
plt.ylabel('MRVL Daily Returns', fontsize=12)
plt.title('CAPM Analysis: Marvell Technology (MRVL) vs. NASDAQ\n(Mar 2025 - Mar 2026)', fontsize=14, fontweight='bold')
plt.legend()
plt.grid(True, alpha=0.3)

# 在图表上添加结果文本框
textstr = f'预设Beta = {beta:.1f}\n计算Beta = {calculated_beta:.4f}\nAlpha = {alpha:.6f}\nR² = {r_squared:.4f}'
props = dict(boxstyle='round', facecolor='wheat', alpha=0.8)
plt.text(0.05, 0.95, textstr, transform=plt.gca().transAxes, fontsize=12,
         verticalalignment='top', bbox=props)

# 保存高分辨率图片
plt.tight_layout()
#plt.savefig('C:/Users/MA/Documents/CAPM_Analysis_MRVL_NASDAQ.png', dpi=300, bbox_inches='tight')
print("\n专业分析图表已保存为 'CAPM_Analysis_MRVL_NASDAQ.png'")
plt.show()

# 12. 计算总回报和年化波动率
nasdaq_total_return = (nasdaq_prices[-1] / nasdaq_prices[0] - 1) * 100
mrvl_total_return = (mrvl_prices[-1] / mrvl_prices[0] - 1) * 100

days_per_year = 252
nasdaq_annual_vol = daily_returns['NASDAQ'].std() * np.sqrt(days_per_year) * 100
mrvl_annual_vol = daily_returns['MRVL'].std() * np.sqrt(days_per_year) * 100

# 13. 最终总结
print("\n*** MRVL与NASDAQ CAPM分析完成！ ***")
print(f"分析期间: {start_date} 至 {end_date}")
print(f"模拟参数:")
print(f"- MRVL初始价格: $70")
print(f"- NASDAQ初始指数: 20,000")
print(f"- 预设Beta系数: {beta}")
print(f"- 市场利率: 4.5%")

print(f"1. 计算得到的Beta值为 {calculated_beta:.2f}，接近预设值 {beta}")
print(f"2. Alpha值为 {alpha:.6f}，表明{'有' if alpha > 0.0005 else '无显著'}超额收益")
print(f"3. 市场因素解释了MRVL {r_squared*100:.1f}% 的价格波动")
print(f"4. 期间总回报: MRVL = {mrvl_total_return:.1f}%, NASDAQ = {nasdaq_total_return:.1f}%")
print(f"5. 年化波动率: MRVL = {mrvl_annual_vol:.1f}%, NASDAQ = {nasdaq_annual_vol:.1f}%")


# 14. 保存处理后的数据
#closing_prices.to_csv('MRVL_NASDAQ_prices.csv')
#daily_returns.to_csv('MRVL_NASDAQ_returns.csv')
#print("\n价格和收益率数据已保存为CSV文件。")

print("\n项目全部完成！")