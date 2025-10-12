#基于BSM模型中对数正态分布与价格游走假设的投资组合蒙特卡洛模拟分析
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import warnings
warnings.filterwarnings('ignore')

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

print("=== 投资组合蒙特卡罗模拟分析 ===")

class PortfolioMonteCarlo:
    def __init__(self):
        self.simulation_results = {}
        
    def get_user_inputs(self):
        """获取用户输入参数"""
        print("\n--- 投资参数输入 ---")
        self.initial_investment = float(input("请输入初始投资金额 (元): "))
        self.annual_return = float(input("请输入预期年化收益率 (%): ")) / 100
        self.volatility = float(input("请输入年化波动率 (%): ")) / 100
        self.years = int(input("请输入投资年限 (年): "))
        self.num_simulations = int(input("请输入模拟次数 (建议1000-10000): "))
        
        # 验证输入合理性
        if self.volatility <= 0:
            print("警告: 波动率应为正数")
        if self.num_simulations < 100:
            print("警告: 模拟次数过少，结果可能不准确")
    
    def run_simulation(self):
        """运行蒙特卡罗模拟"""
        print(f"\n正在运行 {self.num_simulations} 次蒙特卡罗模拟...")
        
        #可填入随机种子以复现结果
        np.random.seed()
        
        # 初始化结果数组
        self.final_values = np.zeros(self.num_simulations)
        self.all_paths = np.zeros((self.num_simulations, self.years + 1))
        self.all_paths[:, 0] = self.initial_investment
        
        # 运行模拟
        for i in range(self.num_simulations):
            # 生成随机收益率路径（BSM推出的对数正态分布）
            random_returns = np.random.normal(
                self.annual_return - 0.5 * self.volatility**2, 
                self.volatility, 
                self.years
            )
            
            # 计算投资价值路径
            path = [self.initial_investment]
            current_value = self.initial_investment
            
            for ret in random_returns:
                current_value *= np.exp(ret)
                path.append(current_value)
            
            self.all_paths[i] = path
            self.final_values[i] = current_value
        
        # 计算关键统计指标
        self.calculate_statistics()
        
        print("模拟完成!")
    
    def calculate_statistics(self):
        """计算统计指标"""
        # 最终价值统计
        self.mean_final = np.mean(self.final_values)
        self.median_final = np.median(self.final_values)
        self.std_final = np.std(self.final_values)
        self.min_final = np.min(self.final_values)
        self.max_final = np.max(self.final_values)
        
        # 收益率统计
        total_returns = (self.final_values - self.initial_investment) / self.initial_investment
        self.mean_return = np.mean(total_returns)
        self.annualized_return = (1 + self.mean_return) ** (1/self.years) - 1
        
        # 风险指标
        self.prob_loss = np.sum(self.final_values < self.initial_investment) / self.num_simulations
        self.var_95 = np.percentile(self.final_values, 5)  # 95%置信水平的VaR
        self.var_99 = np.percentile(self.final_values, 1)  # 99%置信水平的VaR
        
        # 置信区间
        self.ci_90_low = np.percentile(self.final_values, 5)
        self.ci_90_high = np.percentile(self.final_values, 95)
        self.ci_95_low = np.percentile(self.final_values, 2.5)
        self.ci_95_high = np.percentile(self.final_values, 97.5)
    
    def display_results(self):
        """显示模拟结果"""
        print("\n" + "="*50)
        print("蒙特卡罗模拟结果汇总")
        print("="*50)
        
        print(f"\n--- 基础参数 ---")
        print(f"初始投资: {self.initial_investment:,.2f} 元")
        print(f"预期年化收益率: {self.annual_return*100:.2f}%")
        print(f"年化波动率: {self.volatility*100:.2f}%")
        print(f"投资年限: {self.years} 年")
        print(f"模拟次数: {self.num_simulations:,} 次")
        
        print(f"\n--- 最终价值统计 ---")
        print(f"平均最终价值: {self.mean_final:,.2f} 元")
        print(f"中位数最终价值: {self.median_final:,.2f} 元")
        print(f"标准差: {self.std_final:,.2f} 元")
        print(f"最小值: {self.min_final:,.2f} 元")
        print(f"最大值: {self.max_final:,.2f} 元")
        
        print(f"\n--- 收益率分析 ---")
        print(f"平均总收益率: {self.mean_return*100:.2f}%")
        print(f"年化平均收益率: {self.annualized_return*100:.2f}%")
        
        print(f"\n--- 风险评估 ---")
        print(f"亏损概率: {self.prob_loss*100:.2f}%")
        print(f"95% VaR (最坏情况): {self.var_95:,.2f} 元")
        print(f"99% VaR (极端情况): {self.var_99:,.2f} 元")
        
        print(f"\n--- 置信区间 ---")
        print(f"90% 置信区间: [{self.ci_90_low:,.2f}, {self.ci_90_high:,.2f}] 元")
        print(f"95% 置信区间: [{self.ci_95_low:,.2f}, {self.ci_95_high:,.2f}] 元")
    
    def create_visualizations(self):
        """创建可视化图表"""
        fig, axes = plt.subplots(2, 2, figsize=(15, 12))
        fig.suptitle(f'投资组合蒙特卡罗模拟分析 ({self.num_simulations:,}次模拟)', fontsize=16, fontweight='bold')
        
        # 1. 最终价值分布直方图
        axes[0, 0].hist(self.final_values, bins=50, alpha=0.7, color='skyblue', edgecolor='black')
        axes[0, 0].axvline(self.mean_final, color='red', linestyle='--', linewidth=2, label=f'平均值: {self.mean_final:,.0f}元')
        axes[0, 0].axvline(self.initial_investment, color='green', linestyle='--', linewidth=2, label=f'初始投资: {self.initial_investment:,.0f}元')
        axes[0, 0].set_xlabel('最终价值 (元)')
        axes[0, 0].set_ylabel('频数')
        axes[0, 0].set_title('最终价值分布')
        axes[0, 0].legend()
        axes[0, 0].grid(True, alpha=0.3)
        
        # 2. 随机路径样本
        sample_paths = self.all_paths[:100]  # 只显示前100条路径
        years = range(self.years + 1)
        for i in range(min(100, self.num_simulations)):
            axes[0, 1].plot(years, sample_paths[i], alpha=0.1, color='blue')
        
        # 计算平均路径
        mean_path = np.mean(self.all_paths, axis=0)
        axes[0, 1].plot(years, mean_path, color='red', linewidth=3, label='平均路径')
        axes[0, 1].axhline(self.initial_investment, color='green', linestyle='--', label='初始投资')
        axes[0, 1].set_xlabel('投资年限')
        axes[0, 1].set_ylabel('投资价值 (元)')
        axes[0, 1].set_title('随机投资路径样本')
        axes[0, 1].legend()
        axes[0, 1].grid(True, alpha=0.3)
        
        # 3. 累积分布函数
        sorted_values = np.sort(self.final_values)
        cdf = np.arange(1, len(sorted_values) + 1) / len(sorted_values)
        axes[1, 0].plot(sorted_values, cdf, linewidth=2, color='purple')
        axes[1, 0].axvline(self.var_95, color='orange', linestyle='--', label=f'95% VaR: {self.var_95:,.0f}元')
        axes[1, 0].axvline(self.var_99, color='red', linestyle='--', label=f'99% VaR: {self.var_99:,.0f}元')
        axes[1, 0].set_xlabel('最终价值 (元)')
        axes[1, 0].set_ylabel('累积概率')
        axes[1, 0].set_title('累积分布函数 (CDF)')
        axes[1, 0].legend()
        axes[1, 0].grid(True, alpha=0.3)
        
        # 4. 箱线图
        axes[1, 1].boxplot(self.final_values, vert=True, patch_artist=True,
                          boxprops=dict(facecolor='lightblue', color='blue'),
                          medianprops=dict(color='red'))
        axes[1, 1].set_ylabel('最终价值 (元)')
        axes[1, 1].set_title('最终价值箱线图')
        axes[1, 1].grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.show()
        
        # 额外创建一个收益分布图
        plt.figure(figsize=(10, 6))
        returns = (self.final_values - self.initial_investment) / self.initial_investment * 100
        plt.hist(returns, bins=50, alpha=0.7, color='lightgreen', edgecolor='black')
        plt.axvline(0, color='red', linestyle='--', linewidth=2, label='盈亏平衡点')
        plt.axvline(np.mean(returns), color='blue', linestyle='--', linewidth=2, 
                   label=f'平均收益: {np.mean(returns):.2f}%')
        plt.xlabel('总收益率 (%)')
        plt.ylabel('频数')
        plt.title('投资总收益率分布')
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.show()
    
    def sensitivity_analysis(self):
        """敏感性分析：改变关键参数看结果变化"""
        print("\n正在执行敏感性分析...")
        
        # 测试不同的波动率
        volatilities = [self.volatility * 0.5, self.volatility, self.volatility * 1.5]
        vol_results = []
        
        for vol in volatilities:
            # 简化模拟：只运行1000次快速测试
            temp_final_values = []
            for _ in range(1000):
                random_returns = np.random.normal(
                    self.annual_return - 0.5 * vol**2, 
                    vol, 
                    self.years
                )
                final_value = self.initial_investment
                for ret in random_returns:
                    final_value *= np.exp(ret)
                temp_final_values.append(final_value)
            
            vol_results.append({
                'volatility': vol * 100,
                'mean_value': np.mean(temp_final_values),
                'std_value': np.std(temp_final_values),
                'prob_loss': np.sum(np.array(temp_final_values) < self.initial_investment) / 1000
            })
        
        # 显示敏感性分析结果
        print("\n--- 波动率敏感性分析 ---")
        for result in vol_results:
            print(f"波动率 {result['volatility']:.1f}%: "
                  f"平均价值 {result['mean_value']:,.0f}元, "
                  f"亏损概率 {result['prob_loss']*100:.1f}%")

def main():
    """主函数"""
    # 创建模拟实例
    simulator = PortfolioMonteCarlo()
    
    # 获取用户输入
    simulator.get_user_inputs()
    
    # 运行模拟
    simulator.run_simulation()
    
    # 显示结果
    simulator.display_results()
    
    # 创建可视化
    simulator.create_visualizations()
    
    # 执行敏感性分析
    simulator.sensitivity_analysis()
    
    print("\n=== 分析完成 ===")

if __name__ == "__main__":
    main()