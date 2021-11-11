from torch.utils.cpp_extension import load
import os.path as osp
dirname = osp.dirname(__file__)
ray_aabb = load(
    'ray_aabb', ['{}/ray_aabb_cuda.cpp'.format(dirname), '{}/ray_aabb_cuda_kernel.cu'.format(dirname)], verbose=True)
# help(ray_aabb)
