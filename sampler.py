import math
from typing import List

import torch
from ray_utils import RayBundle
from pytorch3d.renderer.cameras import CamerasBase


class StratifiedRaysampler(torch.nn.Module):
    def __init__(self,cfg):
        super().__init__()

        self.n_pts_per_ray = cfg.n_pts_per_ray
        self.min_depth = cfg.min_depth
        self.max_depth = cfg.max_depth

    def forward(self,ray_bundle,):
        """
        stratified (uniform) point sampling along rays
        """
        # TODO (1.4): Compute z values for self.n_pts_per_ray points uniformly sampled between [near, far]
        # ([1, 1, 64, 1])
        z_vals = torch.linspace(self.min_depth, self.max_depth, self.n_pts_per_ray).cuda()

        # TODO (1.4): Sample points from z values
        rays_origins = ray_bundle.origins.reshape(-1, 1, 3).repeat(1, self.n_pts_per_ray, 1)
        rays_dirs = ray_bundle.directions.reshape(-1, 1, 3).repeat(1, self.n_pts_per_ray, 1)
        z_vals = z_vals.reshape(1, -1, 1).repeat(ray_bundle.directions.shape[0], 1, 1)
        sample_points = rays_origins + rays_dirs * z_vals
        
        # Return
        return ray_bundle._replace(
            sample_points=sample_points,
            sample_lengths=z_vals * torch.ones_like(sample_points[..., :1]),
        )


sampler_dict = {
    'stratified': StratifiedRaysampler
}