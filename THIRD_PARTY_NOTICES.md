# Source attribution

## Modified Shepp–Logan phantom

The notebook's `ELLIPSOIDS` parameters and `phantom3d` function are adapted from
`phantom3d.m` by Matthias Christian Schabel, as included in the original MATLAB
source archive `fwd.zip`. The Python adaptation uses sparse array broadcasting,
`float32` voxel values, and `[z, y, x]` storage; the ellipsoid parameters and
rotation convention follow that source.

Original notice:

```text
%   Copyright 2005 Matthias Christian Schabel (matthias @ stanfordalumni . org)
%   University of Utah Department of Radiology
%   Utah Center for Advanced Imaging Research
%   729 Arapeen Drive
%   Salt Lake City, UT 84108-1218
%
%   This code is released under the Gnu Public License (GPL). For more information,
%   see : http://www.gnu.org/copyleft/gpl.html
%
%   Portions of this code are based on phantom.m, copyrighted by the Mathworks
```

The source notice identifies the GPL without specifying a version. It does not
establish a license for the other files in the archive. No repository-wide
license has been selected; the original phantom notice remains applicable to
the adapted material.

## MATLAB development reference

The archive contains `Normal_circ_v2.m`, `s_integral_circ.m`,
`ameliorate_circ.m`, `ameliorate_circ_v2.m`, `xraystreak.m`, and `phantom3d.m`.
The first five files contain no author or license declaration. They informed the
normal-operator and filtering experiment; the archive is not distributed here.
The driver references `Psi.m`, which is absent. The notebook explicitly defines
its smoothing multiplier instead.

## Mathematical reference

David Finch, Ih-Ren Lan and Gunther Uhlmann (2003),
*Microlocal Analysis of the X-Ray Transform with Sources on a Curve*,
Inside Out: Inverse Problems and Applications, MSRI Publications 47, 193–218.
[Chapter PDF](https://library.slmath.org/books/Book47/files/uhlmann.pdf).
