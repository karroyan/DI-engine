"""
Referenced papar <Observe and Look Further: Achieving Consistent Performance on Atari>
"""
import torch


def value_transform(x: torch.Tensor, eps: float = 1e-2) -> torch.Tensor:
    r"""
    Overview:
        :math: `h(x) = sign(x)(\sqrt{(abs(x)+1)} - 1) + \eps * x` .
    """
    return torch.sign(x) * (torch.sqrt(torch.abs(x) + 1) - 1) + eps * x


def value_inv_transform(x: torch.Tensor, eps: float = 1e-2) -> torch.Tensor:
    r"""
    Overview:
        :math: `h^{-1}(x) = sign(x)({(\frac{\sqrt{1+4\eps(|x|+1+\eps)}-1}{2\eps})}^2-1)` .
    """
    return torch.sign(x) * (((torch.sqrt(1 + 4 * eps * (torch.abs(x) + 1 + eps)) - 1) / (2 * eps)) ** 2 - 1)


def symlog(x: torch.Tensor) -> torch.Tensor:
    r"""
    Overview:
        :math: `symlog(x) = sign(x)(\ln{|x|+1})`
    """
    return torch.sign(x) * (torch.log(torch.abs(x) + 1))


def inv_symlog(x: torch.Tensor) -> torch.Tensor:
    r"""
    Overview:
        :math: `symexp(x) = sign(x)(\exp{|x|}-1)`
    """
    return torch.sign(x) * (torch.exp(torch.abs(x)) - 1)
