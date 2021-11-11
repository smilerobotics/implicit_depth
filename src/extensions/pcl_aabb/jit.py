from torch.utils.cpp_extension import load
import os.path as osp
dirname = osp.dirname(__file__)
pcl_aabb = load(
    'pcl_aabb', ['{}/pcl_aabb_cuda.cpp'.format(dirname), '{}/pcl_aabb_cuda_kernel.cu'.format(dirname)], verbose=True)
# help(pcl_aabb)
