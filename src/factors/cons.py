#!/usr/bin/env/ python3
# -*- coding: utf-8 -*-
# @Filename: cons
# @Date:   : 2017-12-06 19:26
# @Author  : YuJun
# @Email   : yujun_mail@163.com

from src.util.dottabledict import DottableDict

# SmartMoney因子的配置参数
SMARTMONEY_CT = DottableDict({'days_num': 10,                               # 计算因子载荷所需分钟行情的天数
                              'db_file': 'Sentiment/SmartQ',                # 因子载荷的保存文件路径名（相对于因子数据库根目录的相对路径）
                              'backtest_path': 'FactorBackTest/SmartQ',     # 历史回测结果文件保存路径
                              'constituent_ratio': 0.1                      # 多头组合的选股比例
                              })
# APM因子的配置参数
APM_CT = DottableDict({'index_code': '000001',                              # 指数代码
                       'days_num': 20,                                      # 计算因子载荷所需分钟行情的天数
                       'db_file': 'Sentiment/APM',                          # 因子载荷的保存文件路径名（相对于因子数据库根目录的相对路径）
                       'backtest_path': 'FactorBackTest/APM',               # 历史回测结果文件的保存路径（相对于因子数据库根目录的相对路径）
                       'constituent_ratio': 0.1                             # 多头组合的选股比例
                       })
# IntradayMementum因子的配置参数
INTRADAYMOMENTUM_CT = DottableDict({'days_num': 20,                                             # 计算因子载荷所需分钟行情的天数
                                    'db_file': 'Momentum/IntradayMomentum/IntradayMomentum',    # 因子载荷的保存文件路径名（相对于因子数据库根目录的相对路径）
                                    'backtest_path': 'FactorBackTest/IntradayMomentum'          # 历史回测结果文件的保存路径（相对于因子数据库根目录的相对路径）
                                    })
# 规模因子的配置参数
SCALE_CT = DottableDict({'db_file': 'ElementaryFactor/Scale/Scale'})
# 传统动量因子的配置参数
MOMENTUM_CT = DottableDict({'short_term_days': '20|60',                 # 短期动量交易日天数
                            'long_term_days': '120|240',                # 长期动量交易日天数
                            'db_file': 'Momentum/Momentum/Momentum',    # 因子载荷的保存文件路径（相对于因子数据库根目录的相对路径）
                            'backtest_path': 'FactorBackTest/Momentum'  # 历史回测结果文件的保存路径（相对于因子数据库根目录的相对路径）
                            })
# 价值因子的配置参数
VALUE_CT = DottableDict({'db_file': 'Value/Value',                      # 因子载荷的保存文件相对路径
                         'backtest_path': 'FactorBackTest/Value'        # 历史回测结果文件的相对保存路径
                         })
# 因子数据库的路径
# FACTOR_DB = DottableDict({'db_path': '/Users/davidyujun/Dropbox/FactorDB'})
FACTOR_DB = DottableDict({'db_path': '/Volumes/DB/FactorDB'})


if __name__ == '__main__':
    pass
