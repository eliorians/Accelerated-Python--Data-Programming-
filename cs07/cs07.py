
import matplotlib.pyplot as plt
import numpy as np


#1.1
def construct_file_name(lat, lon):
    filename = 'USGS_NED_1_'
    
    #lat formatting
    if lat < 0:
        filename = filename + 's' + str(lat*-1)
    else:
        filename = filename + 'n' + str(lat)

    #lon formatting
    if (abs(lon) < 100):
        if lon < 0:
            filename = filename + 'w0' + str(lon*-1)
        else:
            filename = filename + 'e0' + str(lon)
    else:
        if lon < 0:
            filename = filename + 'w' + str(lon*-1)
        else:
            filename = filename + 'e' + str(lon)

    filename = filename + '_IMG.tif'
    return filename



#1.2
def load_trim_image(lat, lon):
    im = plt.imread(construct_file_name(lat, lon))
    im = im[6:-6, 6:-6]

    return im


#1.3
def stitch_four(lat, lon):
    im1 = load_trim_image(lat, lon)
    im2 = load_trim_image(lat, lon+1)
    im3 = load_trim_image(lat-1, lon)
    im4 = load_trim_image(lat-1, lon+1)

    t = np.concatenate((im1, im2), axis = 1)
    b = np.concatenate((im3, im4), axis = 1)
    im = np.concatenate((t, b), axis = 0)

    return im


#1.4
def get_row(lat, lon_min, num_tiles):
    
    im = load_trim_image(lat, lon_min)
    for i in range(1, num_tiles):
        im = np.hstack((im, load_trim_image(lat, lon_min+i)))
    
    return im


#1.5
def get_tile_grid(lat_max, lon_min, num_lat, num_lon):
    
    im = get_row(lat_max, lon_min, num_lon)
    for i in range(1, num_lat):
        im = np.vstack((im, get_row(lat_max-i, lon_min, num_lon)))
    
    return im

#1.6
def get_northwest(lat, lon):

    #lat rounding
    if (not is_whole(lat)):
        lat = int(str(lat).split('.')[0])
        if (lat > 0):
            lat = lat + 1
        else:
            lat = lat - 1
    else:
        lat = int(lat)

    #lon rounding
    if (not is_whole(lon)):
        lon = int(str(lon).split('.')[0])
        if (lon > 0):
            lon = lon + 1
        else:
            lon = lon - 1
    else:
        lon = int(lon)

    return (lat, lon)

def is_whole(n):
    return n % 1 == 0

#1.7
def get_tile_grid_decimal(northwest, southeast):

    (la1, lo1) = northwest
    (la2, lo2) = southeast
    
    lat1, lon1 = get_northwest(la1, lo1)
    lat2, lon2 = get_northwest(la2, lo2)

    num_lat = abs(lat2-lat1)
    num_lon = abs(lon2-lon1)

    return get_tile_grid(lat1, lon1, num_lat+1, num_lon+1)


# -- Testing Section 1 -- #

# print('1.1 testing')
# print(construct_file_name(lat=36, lon=-82))
# print(" == ")
# print("USGS_NED_1_n36w082_IMG.tif\n")
# print(construct_file_name(lat=-36, lon=82))
# print(" == ")
# print("USGS_NED_1_s36e082_IMG.tif\n")


# print('1.2 testing')
# im = load_trim_image(lat=38, lon=-84)
# print(im.shape)
# h, w = im.shape
# print(im[h//2-5:h//2+5, w//2-5:w//2+5])
# print(im[:10, :10])
# plt.imshow(im[:32,:32])
# plt.colorbar()
# plt.show()

# print('1.3 testing')
# im = stitch_four(37, -83)
# print(im.shape)
# h, w = im.shape
# print(im[h//2-5:h//2+5, w//2-5:w//2+5])
# plt.imshow(im[h//2-16:h//2+16, w//2-16:w//2+16])
# plt.colorbar()
# plt.show()
# plt.imshow(im)
# plt.colorbar()
# plt.show()

# print("1.4 testing")
# im = get_row(lat=38, lon_min=-84, num_tiles=1)
# print(im.shape)
# h, w = im.shape
# print(im[h//2-5:h//2+5, w//2-5:w//2+5])
# plt.imshow(im[h//2-16:h//2+16, w//2-16:w//2+16])
# plt.colorbar()
# plt.show()
# plt.imshow(im)
# plt.colorbar()
# plt.show()

# print("1.5 testing")
# im = get_tile_grid(lat_max=37, lon_min=-83, num_lat=2, num_lon=2)
# im.shape
# h, w = im.shape
# print(im[h//2-5:h//2+5, w//2-5:w//2+5])
# plt.imshow(im[h//2-16:h//2+16, w//2-16:w//2+16])
# plt.colorbar()
# plt.show()
# plt.imshow(im)
# plt.colorbar()
# plt.show()

# print("1.6 testing")
# print(get_northwest(lat=36.211389, lon=-81.668611))
# print('==')
# print("(37, -82)\n")

# print('1.7 testing')
# nw = (37.2, -82.7)
# se = (36.6, -82.5)
# im = get_tile_grid_decimal(nw, se)
# print(im.shape)
# nw = (37.2, -83.7)
# se = (36.6, -81.5)
# im = get_tile_grid_decimal(nw, se)
# print(im.shape)
# nw = (37.5, -82.5)
# se = (36.5, -81.5)
# im = get_tile_grid_decimal(nw, se)
# print(im.shape)
# h, w = im.shape
# print(im[h//2-5:h//2+5, w//2-5:w//2+5])
# plt.imshow(im[h//2-16:h//2+16, w//2-16:w//2+16])
# plt.colorbar()
# plt.show()
# plt.imshow(im)
# plt.colorbar()
# plt.show()


#2.1
def dec_to_dms(dec):

    is_positive = dec >= 0
    dec = abs(dec)
    minutes,seconds = divmod(dec*3600,60)
    degrees,minutes = divmod(minutes,60)
    degrees = degrees if is_positive else -degrees
    
    return (degrees,np.round(minutes),np.round(seconds))


#2.2
def seconds_to_index(seconds):

    if (seconds == 0):
        return 0
    else:
        return 3600-seconds

#2.3
def get_trim(northwest, southeast):
    
    t, l = northwest
    b, r = southeast
    
    t = int(t)
    l = int(l)
    b = int(b)
    r = int(r)

    tdeg, tmin, tsec = dec_to_dms(t)
    tsec = tsec + (tmin * 60)
    top = seconds_to_index(tsec)

    ldeg, lmin, lsec = dec_to_dms(l)
    lsec = lsec + (lmin * 60)
    left = seconds_to_index(lsec)

    bdeg, bmin, bsec = dec_to_dms(b)
    bsec = bsec + (bmin * 60)
    bottom = 3599 - seconds_to_index(bsec)

    rdeg, rmin, rsec = dec_to_dms(r)
    rsec = rsec + (rmin * 60)
    right = 3599 - seconds_to_index(rsec)

    return left, right, bottom, top

#2.4
def get_roi(center, n):
    
    lat, lon = center

    northwest = ((n/3600 + lat),-(n/3600 - lon))
    southeast = (-(n/3600 - lat),(n/3600 + lon))
    
    return northwest, southeast

#2.5
def crop(im, trim):
    l, r, b, t = trim

    if (l != 0):
        im = im[ : , l:  ]
    if (r != 0):
        im = im[ :  , :-r]
    if (b != 0):
        im = im[ :-b, :  ]
    if (t != 0):
        im = im[ t: , :  ]

    
    return im

#2.6
def get_extent(northwest, southeast):

    top , left = northwest
    bottom, right = southeast
    return left, right, bottom, top


#2.7
def zoom(center, n):

    nw, se = get_roi(center, n)
    im = get_tile_grid_decimal(nw, se)
    trim = get_trim(nw, se)
    im = crop(im, trim)

    return get_extent(nw, se), im




#--- Testing Section 2 ---#

# print("Testing 2.1")
# print(dec_to_dms(0.005555555525127431))
# print("==")
# print("(0.0, 0, 20)\n")


# print("Testing 2.2")
# print(seconds_to_index(0))
# print("==")
# print("0\n")


# print("Testing 2.3")
# nw = (36, -82)
# se = (35+1/3600, -81-1/3600)
# print(get_trim(nw, se))
# print("==")
# print("0, 0, 0, 0\n")
# nw = (36-4/3600, -82+1/3600)
# se = (35+4/3600, -81-3/3600)
# print(get_trim(nw, se))
# print("==")
# print("1, 2, 3, 4\n")
# nw = (38-4/3600, -84+1/3600)
# se = (32+4/3600, -80-3/3600)
# print(get_trim(nw, se))
# print("==")
# print("1, 2, 3, 4\n")

# print("Testing 2.4")
# center = (35+3601/7200, -81-3601/7200)
# print(get_roi(center, 1799.5))
# print("((36.0, -82.0),(35.00027777777778, -81.00027777777777))\n")
# center = (29.48472222222222, -122.2688888888889)
# print(get_roi(center, 0))
# print("((29.48472222222222, -122.2688888888889), (29.48472222222222, -122.2688888888889))")

# print("Testing 2.5")
# print("im: ")
# im = np.arange(64).reshape((8, 8))
# print(im)
# print(im.shape)
# print("\n")
# print("im2: ")
# im2 = crop(im, (1, 2, 3, 4))
# print(im2)
# print(im2.shape)
# print("\n")
# print("im3: ")
# im3 = crop(im, (0, 0, 0, 0))
# print(im3)
# print(im3.shape)
# print("\n")

# print("Testing 2.6")
# nw = (36, -83)
# se = (34, -81)
# print(get_extent(nw, se))
# print("(-83, -81, 34, 36)")

# print("Testing 2.7")
# extent, im = zoom(center=(36.211389, -81.668611), n=100)
# plt.imshow(im, extent=extent)
# plt.colorbar()
# plt.show()