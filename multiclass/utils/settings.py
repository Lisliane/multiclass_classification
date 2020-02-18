""" Constants used in the processes """

# Authors: Lisliane Zanette de Oliveira <lislianezanetteoliveira@gmail.com>

# Managing files
PATCH_SOURCE = 'in'
PATCH_DESTINY = 'out/edited'
DESTINY_PDF = 'out/result/out.pdf'
EXTENSION_TO_EDIT = '.png'
EXTENSION_TO_OUTPUT = '.png'

# Flags
RUN_HISTOGRAM_EQUALIZATION = True
RUN_RETINEX = False
RUN_CROP = False
RUN_ROTATE = False

# Image - Retinex
RETINEX_MAX_SCALE = 14069
RETINEX_NR_SCALE = 3
RETINEX_ALPHA = 128.
RETINEX_GAIN = 1.
RETINEX_OFFSET = 0.
RETINEX_DYNAMIC = 2.0

# Image - Rotate
ROTATE_SIGMA = 0.33
ROTATE_APERTURE_SIZE = 3
ROTATE_HLP_RHO = 1
ROTATE_HLP_THRESHOLD = 100
ROTATE_HLP_MIN_LINE_LENGTH = 100
ROTATE_HLP_MAX_LINE_GAP = 5

# Image - Histogram equalization
HE_CLIP_LIMIT = 2.0
HE_TILE_GRID_SIZE = 4

# Image - Crop
CROP_THRESHOLD = 'BINARY'
CROP_THRESHOLD_BLOCK_SIZE = 7
CROP_THRESHOLD_C = 2
CROP_THRESHOLD_VALUE = 128
CROP_THRESHOLD_MAX = 255

# PDF
PDF_X = 20
PDF_Y = 20
