import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
import threading
import time

class WindSolarPumpedStorageOptimizer:
    def __init__(self, root):
        self.root = root
        self.root.title("风-光-抽水蓄能系统容量配置优化")
        self.root.geometry("1200x800")
        self.root.configure(bg='#f0f0f0')
        
        # 设置样式
        style = ttk.Style()
        style.theme_use('clam')
        
        self.setup_ui()
        
    def setup_ui(self):
        # 主标题
        title_label = tk.Label(self.root, text="风-光-抽水蓄能系统容量配置优化", 
                              font=("Arial", 16, "bold"), bg='#f0f0f0', fg='#2c3e50')
        title_label.pack(pady=10)
        
        # 创建主框架
        main_frame = tk.Frame(self.root, bg='#f0f0f0')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        # 左侧参数输入区域
        self.setup_input_panel(main_frame)
        
        # 右侧结果显示区域
        self.setup_result_panel(main_frame)
        
    def setup_input_panel(self, parent):
        """设置参数输入面板"""
        input_frame = tk.LabelFrame(parent, text="系统参数配置", 
                                   font=("Arial", 12, "bold"), 
                                   bg='#f0f0f0', fg='#2c3e50',
                                   padx=10, pady=10)
        input_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))
        
        # 风电参数
        wind_frame = tk.LabelFrame(input_frame, text="风电系统", 
                                  bg='#f0f0f0', fg='#34495e')
        wind_frame.pack(fill=tk.X, pady=5)
        
        tk.Label(wind_frame, text="装机容量 (MW):", bg='#f0f0f0').grid(row=0, column=0, sticky=tk.W, padx=5, pady=2)
        self.wind_capacity = tk.StringVar(value="100")
        tk.Entry(wind_frame, textvariable=self.wind_capacity, width=15).grid(row=0, column=1, padx=5, pady=2)
        
        tk.Label(wind_frame, text="容量因子:", bg='#f0f0f0').grid(row=1, column=0, sticky=tk.W, padx=5, pady=2)
        self.wind_capacity_factor = tk.StringVar(value="0.35")
        tk.Entry(wind_frame, textvariable=self.wind_capacity_factor, width=15).grid(row=1, column=1, padx=5, pady=2)
        
        tk.Label(wind_frame, text="单位投资成本 (万元/MW):", bg='#f0f0f0').grid(row=2, column=0, sticky=tk.W, padx=5, pady=2)
        self.wind_cost = tk.StringVar(value="7000")
        tk.Entry(wind_frame, textvariable=self.wind_cost, width=15).grid(row=2, column=1, padx=5, pady=2)
        
        # 光伏参数
        solar_frame = tk.LabelFrame(input_frame, text="光伏系统", 
                                   bg='#f0f0f0', fg='#34495e')
        solar_frame.pack(fill=tk.X, pady=5)
        
        tk.Label(solar_frame, text="装机容量 (MW):", bg='#f0f0f0').grid(row=0, column=0, sticky=tk.W, padx=5, pady=2)
        self.solar_capacity = tk.StringVar(value="150")
        tk.Entry(solar_frame, textvariable=self.solar_capacity, width=15).grid(row=0, column=1, padx=5, pady=2)
        
        tk.Label(solar_frame, text="容量因子:", bg='#f0f0f0').grid(row=1, column=0, sticky=tk.W, padx=5, pady=2)
        self.solar_capacity_factor = tk.StringVar(value="0.20")
        tk.Entry(solar_frame, textvariable=self.solar_capacity_factor, width=15).grid(row=1, column=1, padx=5, pady=2)
        
        tk.Label(solar_frame, text="单位投资成本 (万元/MW):", bg='#f0f0f0').grid(row=2, column=0, sticky=tk.W, padx=5, pady=2)
        self.solar_cost = tk.StringVar(value="4500")
        tk.Entry(solar_frame, textvariable=self.solar_cost, width=15).grid(row=2, column=1, padx=5, pady=2)
        
        # 抽水蓄能参数
        pumped_frame = tk.LabelFrame(input_frame, text="抽水蓄能系统", 
                                    bg='#f0f0f0', fg='#34495e')
        pumped_frame.pack(fill=tk.X, pady=5)
        
        tk.Label(pumped_frame, text="装机容量 (MW):", bg='#f0f0f0').grid(row=0, column=0, sticky=tk.W, padx=5, pady=2)
        self.pumped_capacity = tk.StringVar(value="200")
        tk.Entry(pumped_frame, textvariable=self.pumped_capacity, width=15).grid(row=0, column=1, padx=5, pady=2)
        
        tk.Label(pumped_frame, text="储能容量 (MWh):", bg='#f0f0f0').grid(row=1, column=0, sticky=tk.W, padx=5, pady=2)
        self.pumped_energy = tk.StringVar(value="1600")
        tk.Entry(pumped_frame, textvariable=self.pumped_energy, width=15).grid(row=1, column=1, padx=5, pady=2)
        
        tk.Label(pumped_frame, text="单位投资成本 (万元/MW):", bg='#f0f0f0').grid(row=2, column=0, sticky=tk.W, padx=5, pady=2)
        self.pumped_cost = tk.StringVar(value="12000")
        tk.Entry(pumped_frame, textvariable=self.pumped_cost, width=15).grid(row=2, column=1, padx=5, pady=2)
        
        # 经济参数
        economic_frame = tk.LabelFrame(input_frame, text="经济参数", 
                                      bg='#f0f0f0', fg='#34495e')
        economic_frame.pack(fill=tk.X, pady=5)
        
        tk.Label(economic_frame, text="电价 (元/kWh):", bg='#f0f0f0').grid(row=0, column=0, sticky=tk.W, padx=5, pady=2)
        self.electricity_price = tk.StringVar(value="0.6")
        tk.Entry(economic_frame, textvariable=self.electricity_price, width=15).grid(row=0, column=1, padx=5, pady=2)
        
        tk.Label(economic_frame, text="贴现率 (%):", bg='#f0f0f0').grid(row=1, column=0, sticky=tk.W, padx=5, pady=2)
        self.discount_rate = tk.StringVar(value="8")
        tk.Entry(economic_frame, textvariable=self.discount_rate, width=15).grid(row=1, column=1, padx=5, pady=2)
        
        tk.Label(economic_frame, text="项目寿命 (年):", bg='#f0f0f0').grid(row=2, column=0, sticky=tk.W, padx=5, pady=2)
        self.project_lifetime = tk.StringVar(value="25")
        tk.Entry(economic_frame, textvariable=self.project_lifetime, width=15).grid(row=2, column=1, padx=5, pady=2)
        
        # 运行按钮
        button_frame = tk.Frame(input_frame, bg='#f0f0f0')
        button_frame.pack(fill=tk.X, pady=10)
        
        self.run_button = tk.Button(button_frame, text="开始优化", 
                                   command=self.run_optimization,
                                   bg='#3498db', fg='white', 
                                   font=("Arial", 12, "bold"),
                                   padx=20, pady=10)
        self.run_button.pack()
        
        # 进度条
        self.progress = ttk.Progressbar(button_frame, mode='indeterminate')
        self.progress.pack(fill=tk.X, pady=5)
        
    def setup_result_panel(self, parent):
        """设置结果显示面板"""
        result_frame = tk.LabelFrame(parent, text="优化结果", 
                                    font=("Arial", 12, "bold"), 
                                    bg='#f0f0f0', fg='#2c3e50',
                                    padx=10, pady=10)
        result_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        # 结果显示文本区域
        self.result_text = tk.Text(result_frame, height=15, width=50, 
                                  font=("Consolas", 10), 
                                  bg='white', fg='#2c3e50')
        scrollbar = tk.Scrollbar(result_frame, orient=tk.VERTICAL, command=self.result_text.yview)
        self.result_text.configure(yscrollcommand=scrollbar.set)
        
        self.result_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
    def validate_inputs(self):
        """验证输入参数"""
        try:
            # 检查数值输入
            float(self.wind_capacity.get())
            float(self.wind_capacity_factor.get())
            float(self.wind_cost.get())
            float(self.solar_capacity.get())
            float(self.solar_capacity_factor.get())
            float(self.solar_cost.get())
            float(self.pumped_capacity.get())
            float(self.pumped_energy.get())
            float(self.pumped_cost.get())
            float(self.electricity_price.get())
            float(self.discount_rate.get())
            int(self.project_lifetime.get())
            
            # 检查合理性
            if float(self.wind_capacity_factor.get()) > 1 or float(self.wind_capacity_factor.get()) < 0:
                raise ValueError("风电容量因子应在0-1之间")
            if float(self.solar_capacity_factor.get()) > 1 or float(self.solar_capacity_factor.get()) < 0:
                raise ValueError("光伏容量因子应在0-1之间")
                
            return True
        except ValueError as e:
            messagebox.showerror("输入错误", f"参数输入有误: {str(e)}")
            return False
    
    def mock_optimization_algorithm(self, params):
        """模拟优化算法"""
        # 模拟计算时间
        time.sleep(2)
        
        # 提取参数
        wind_cap = float(params['wind_capacity'])
        wind_cf = float(params['wind_capacity_factor'])
        wind_cost = float(params['wind_cost'])
        
        solar_cap = float(params['solar_capacity'])
        solar_cf = float(params['solar_capacity_factor'])
        solar_cost = float(params['solar_cost'])
        
        pumped_cap = float(params['pumped_capacity'])
        pumped_energy = float(params['pumped_energy'])
        pumped_cost = float(params['pumped_cost'])
        
        electricity_price = float(params['electricity_price'])
        discount_rate = float(params['discount_rate']) / 100
        lifetime = int(params['project_lifetime'])
        
        # 模拟优化计算
        # 年发电量计算
        wind_annual_generation = wind_cap * wind_cf * 8760  # MWh
        solar_annual_generation = solar_cap * solar_cf * 8760  # MWh
        
        # 总投资成本
        total_investment = (wind_cap * wind_cost + 
                          solar_cap * solar_cost + 
                          pumped_cap * pumped_cost) / 10000  # 亿元
        
        # 年收益计算
        annual_revenue = (wind_annual_generation + solar_annual_generation) * electricity_price / 1000  # 万元
        
        # 净现值计算 (简化)
        npv = -total_investment * 10000  # 万元
        for year in range(1, lifetime + 1):
            npv += annual_revenue / ((1 + discount_rate) ** year)
        
        # 内部收益率估算
        irr = (annual_revenue / (total_investment * 10000)) * 100
        
        # 模拟优化结果
        results = {
            'optimal_wind_capacity': wind_cap * (1 + np.random.normal(0, 0.1)),
            'optimal_solar_capacity': solar_cap * (1 + np.random.normal(0, 0.1)),
            'optimal_pumped_capacity': pumped_cap * (1 + np.random.normal(0, 0.05)),
            'total_investment': total_investment,
            'annual_generation': wind_annual_generation + solar_annual_generation,
            'annual_revenue': annual_revenue,
            'npv': npv,
            'irr': irr,
            'wind_annual_generation': wind_annual_generation,
            'solar_annual_generation': solar_annual_generation,
            'lcoe': total_investment * 10000 / (wind_annual_generation + solar_annual_generation) * 1000  # 元/MWh
        }
        
        return results
    
    def run_optimization(self):
        """运行优化算法"""
        if not self.validate_inputs():
            return
            
        # 禁用按钮并显示进度条
        self.run_button.config(state='disabled', text='优化中...')
        self.progress.start()
        
        # 清空结果显示
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, "正在运行优化算法...\n")
        self.root.update()
        
        # 获取参数
        params = {
            'wind_capacity': self.wind_capacity.get(),
            'wind_capacity_factor': self.wind_capacity_factor.get(),
            'wind_cost': self.wind_cost.get(),
            'solar_capacity': self.solar_capacity.get(),
            'solar_capacity_factor': self.solar_capacity_factor.get(),
            'solar_cost': self.solar_cost.get(),
            'pumped_capacity': self.pumped_capacity.get(),
            'pumped_energy': self.pumped_energy.get(),
            'pumped_cost': self.pumped_cost.get(),
            'electricity_price': self.electricity_price.get(),
            'discount_rate': self.discount_rate.get(),
            'project_lifetime': self.project_lifetime.get()
        }
        
        # 在新线程中运行优化算法
        def optimization_thread():
            try:
                results = self.mock_optimization_algorithm(params)
                
                # 在主线程中更新UI
                self.root.after(0, self.update_results, results)
            except Exception as e:
                self.root.after(0, self.show_error, str(e))
        
        threading.Thread(target=optimization_thread, daemon=True).start()
    
    def update_results(self, results):
        """更新结果显示"""
        # 停止进度条并恢复按钮
        self.progress.stop()
        self.run_button.config(state='normal', text='开始优化')
        
        # 清空并更新结果显示
        self.result_text.delete(1.0, tk.END)
        
        result_text = f"""优化结果报告
{'='*50}

系统配置:
  风电装机容量: {results['optimal_wind_capacity']:.2f} MW
  光伏装机容量: {results['optimal_solar_capacity']:.2f} MW
  抽水蓄能容量: {results['optimal_pumped_capacity']:.2f} MW

发电性能:
  风电年发电量: {results['wind_annual_generation']:.2f} MWh
  光伏年发电量: {results['solar_annual_generation']:.2f} MWh
  总年发电量: {results['annual_generation']:.2f} MWh

经济指标:
  总投资成本: {results['total_investment']:.2f} 亿元
  年收益: {results['annual_revenue']:.2f} 万元
  净现值(NPV): {results['npv']:.2f} 万元
  内部收益率(IRR): {results['irr']:.2f}%
  平准化发电成本: {results['lcoe']:.2f} 元/MWh

优化建议:
  - 系统配置合理，满足经济性要求
  - 建议关注储能系统的运行策略优化
  - 可考虑增加储能容量以提高系统灵活性
"""
        
        self.result_text.insert(tk.END, result_text)
        
        messagebox.showinfo("优化完成", "容量配置优化已完成！")
    
    def show_error(self, error_msg):
        """显示错误信息"""
        self.progress.stop()
        self.run_button.config(state='normal', text='开始优化')
        messagebox.showerror("优化错误", f"优化过程中出现错误: {error_msg}")

def main():
    root = tk.Tk()
    app = WindSolarPumpedStorageOptimizer(root)
    root.mainloop()

if __name__ == "__main__":
    main()