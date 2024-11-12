"""
重新组织 UDIS-D-E 数据集中的 WhiteCar 数据集，空间顺序改为时间顺序
按时间顺序组织：每个文件夹里保存的是单个相机在不同时刻的数据
按空间顺序组织：每个文件夹里保存的是同一时刻下不同相机的数据
"""

import os
import numpy as np
from collections import OrderedDict
from tqdm import tqdm
import shutil
from loguru import logger
import random

#! 设置参数
DATASET_ROOT = '/home/dzp62442/Projects/UnsupervisedDeepImageStitching/Datasets'  # Datasets 文件夹
ORIGIN_DIR = os.path.join(DATASET_ROOT, "UDIS-D-E", "WhiteCar")  # 原始 SV-UDIS-D 数据集中的 WhiteCar 数据集路径
REORGANIZED_DIR = os.path.join(DATASET_ROOT, "WhiteCar-spa")  # 重新组织后的数据集路径

def main():
    logger.info(f"Reorganizing WhiteCar dataset from {ORIGIN_DIR} to {REORGANIZED_DIR} ...")
    for mode in ['training', 'testing']:  #! 遍历训练集和测试集
        src_group_num = len(os.listdir(os.path.join(ORIGIN_DIR, mode)))  # 训练或测试集中的图像组数量
        dst_input_1 = os.path.join(REORGANIZED_DIR, mode, 'input1')
        os.makedirs(dst_input_1, exist_ok=True)
        dst_input_2 = os.path.join(REORGANIZED_DIR, mode, 'input2')
        os.makedirs(dst_input_2, exist_ok=True)
        for group_idx in tqdm(range(src_group_num)):  #! 遍历训练集或测试集中的每个组
            src_group_dir = os.path.join(ORIGIN_DIR, mode, str(group_idx).zfill(5))  # 当前组的路径
            src_group_img_names = os.listdir(src_group_dir)  # 当前组中的所有图像名称
            src_group_img_names.sort()
            shutil.copyfile(os.path.join(src_group_dir, src_group_img_names[0]), os.path.join(dst_input_1, str(group_idx).zfill(6)+".jpg"))  # 拷贝第一张图片
            shutil.copyfile(os.path.join(src_group_dir, src_group_img_names[1]), os.path.join(dst_input_2, str(group_idx).zfill(6)+".jpg"))  # 拷贝第二张图片
        logger.info(f"Finish processing {mode} set of WhiteCar dataset .")
        logger.info("-----------------------------------------------------------------")


if __name__ == "__main__":
    main()