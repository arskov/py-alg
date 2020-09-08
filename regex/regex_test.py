import re

pat = re.compile("^([a-z_\d]+)_\d+$")

str1 = "interpolation_high_fhd_1"
mat1 = pat.match(str1)
print(str1, mat1.group(1), sep = " => ")

str2 = "f_update_fr3_high_fhd_1"
mat2 = pat.match(str2)
print(str2, mat2.group(1), sep = " => ")

str3 = "face_track_low_fhd_lf2_1"
mat3 = pat.match(str3)
print(str3, mat3.group(1), sep = " => ")