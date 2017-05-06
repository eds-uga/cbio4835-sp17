import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as ndimg
from scipy import stats
import skimage.morphology as morphology
import skimage.filters as filters
import skimage.measure as measure
import skimage.feature as feature
import os
import glob

path_control = "/python/SkelCount/control_images"
path_NPEX = "/python/SkelCount/NPEX_images"
control_reps = []										#Empty lists for replicate subfolders and final paths to loop through
NPEX_reps = []
control_paths = []
NPEX_paths = []
for root, dirs, files in os.walk(path_control):			#Walk through folder to list subfolders (replicates)
    for folder in dirs:
       control_reps.append(folder)

for root, dirs, files in os.walk(path_NPEX):
    for folder in dirs:
        NPEX_reps.append(folder)

for rep in control_reps:								#Populate list with all replicate paths
	control_paths.append(path_control + "/" + rep)

for rep in NPEX_reps:
	NPEX_paths.append(path_NPEX + "/" + rep)

def cellcount(path_control, path_NPEX):
	cellcount_control_avg = []
	cellcount_NPEX_avg = []
	for path in control_paths:
		cellcount_control = []													#Empty list to store control group counts
		for filename in glob.glob(os.path.join(path, "*.jpg")):										#Loop through control folder and open all (and only) JPEGs
			img = ndimg.imread(filename)																	#Read image as numpy array
			nuc = img[:, :, 2] 																				#Slice blue channel (Hoescht)
			thresh_local = filters.threshold_local(nuc, block_size = 55)									#Adaptive/local threshold (arbitrary block_size)
			nuc_bin = nuc > thresh_local 																	#Binarize based on local threshold
			erode = morphology.erosion(nuc_bin)																#Erode (3x) to remove noise
			erode2 = morphology.erosion(erode)
			erode3 = morphology.erosion(erode2)
			distmap = ndimg.distance_transform_edt(erode3) 													#Create distance map of objects
			maxima = feature.peak_local_max(distmap, indices = False, min_distance = 2, labels = erode3)	#Locate maxima to use as watershed seeds
			markers = ndimg.label(maxima)[0]																#Designate maxima as seeds
			labels = morphology.watershed(-distmap, markers, mask = erode3)									#Watershed to separate/identify objects (nuclei)

			regions = measure.regionprops(labels)								#Measure/count objects from watershed to determine initial cell count
			regions_filtered = []												#Loop through list of objects and check size/area (in pixels)
			for i in range(0, len(regions)):									#Set size threshold to filter out noise and anything unlikely to be a cell
				if regions[i].area >= 50: 										#Note: Arbitrary threshold based on trial and error and comparison to prior manual count
					regions_filtered.append(regions[i].area) 					#Populate new list with filtered objects											
			cellcount_control.append(len(regions_filtered))						#Append filtered cell count to list
		cc_control_array = np.array(cellcount_control)
		cellcount_control_avg.append(cc_control_array.mean())

	for path in NPEX_paths:
		cellcount_NPEX = []														#Empty list to store NPEX group counts
		for filename in glob.glob(os.path.join(path, "*.jpg")):										#Loop through NPEX folder and open all (and only) JPEGs
			img = ndimg.imread(filename)																	#Read image as numpy array
			nuc = img[:, :, 2] 																				#Slice blue channel (Hoescht)
			thresh_local = filters.threshold_local(nuc, block_size = 55)									#Adaptive/local threshold (arbitrary block_size)
			nuc_bin = nuc > thresh_local 																	#Binarize based on local threshold
			erode = morphology.erosion(nuc_bin)																#Erode (3x) to remove noise
			erode2 = morphology.erosion(erode)
			erode3 = morphology.erosion(erode2)
			distmap = ndimg.distance_transform_edt(erode3) 													#Create distance map of objects
			maxima = feature.peak_local_max(distmap, indices = False, min_distance = 2, labels = erode3)	#Locate maxima to use as watershed seeds
			markers = ndimg.label(maxima)[0]																#Designate maxima as seeds
			labels = morphology.watershed(-distmap, markers, mask = erode3)									#Watershed to separate/identify objects (nuclei)

			regions = measure.regionprops(labels)								#Measure/count objects from watershed to determine initial cell count
			regions_filtered = []												#Loop through list of objects and check size/area (in pixels)
			for i in range(0, len(regions)):									#Set size threshold to filter out noise and anything unlikely to be a cell
				if regions[i].area >= 50: 										#Note: Arbitrary threshold based on trial and error and comparison to prior manual count
					regions_filtered.append(regions[i].area) 					#Populate new list with filtered objects
			cellcount_NPEX.append(len(regions_filtered))						#Append filtered cell count to list
		cc_NPEX_array = np.array(cellcount_NPEX)
		cellcount_NPEX_avg.append(cc_NPEX_array.mean())

	ttest_cc = stats.ttest_ind(cellcount_control_avg, cellcount_NPEX_avg, equal_var = False)	#T-test between control and NPEX groups

	cellcount_plots = [cellcount_control_avg, cellcount_NPEX_avg]		#Plot boxplots for control vs. NPEX
	plt.subplot(3, 1, 1)
	plt.boxplot(cellcount_plots, patch_artist = True)
	plt.title("Cell Count - NPEX vs. Control")
	plt.xlabel(ttest_cc, color = "red")							#Print t-test results under boxplots
	plt.ylabel("Average cell count")
	plt.xticks([1, 2], ["Control", "NPEX"])

def skeletonize(path_control, path_NPEX):
	skel_control_avg = []
	skel_NPEX_avg = []
	for path in control_paths:
		skel_control = []
		for filename in glob.glob(os.path.join(path, "*.jpg")):
			img = ndimg.imread(filename)
			factin = img[:, :, 1]												#Green channel - f-actin
			thresh_local = filters.threshold_local(factin, block_size = 25)		#Adaptive/Local threshold
			factin_bin = thresh_local > 30										#Binarize based on local threshold
			skel = morphology.skeletonize_3d(factin_bin)						#Skeletonize from binary image

			skel_count = measure.label(skel, return_num = True)					#Count number of skeletons
			skel_area = measure.regionprops(skel_count[0])						#Calculate area of skeletons
			skel_area_filtered = []												#Loop through list of skeletons and check size/area (in pixels)
			for i in range(0, len(skel_area)):									#Set size threshold to filter out noise and small areas unlikely to be part of network
				if skel_area[i].area >= 10: 										
					skel_area_filtered.append(skel_area[i].area)
			safnp = np.array(skel_area_filtered)								#Convert filtered skeleton areas (lengths) to numpy array
			skel_control.append(safnp.sum())								#Append list with total sum of lengths
		skel_control_array = np.array(skel_control)
		skel_control_avg.append(skel_control_array.mean())	

	for path in NPEX_paths:
		skel_NPEX = []
		for filename in glob.glob(os.path.join(path, "*.jpg")):
			img = ndimg.imread(filename)
			factin = img[:, :, 1]												#Green channel - f-actin
			thresh_local = filters.threshold_local(factin, block_size = 25)		#Adaptive/Local threshold
			factin_bin = thresh_local > 30										#Binarize based on local threshold
			skel = morphology.skeletonize_3d(factin_bin)						#Skeletonize from binary image

			skel_count = measure.label(skel, return_num = True)					#Count number of skeletons

			skel_area = measure.regionprops(skel_count[0])						#Calculate area of skeletons

			skel_area_filtered = []												#Loop through list of skeletons and check size/area (in pixels)
			for i in range(0, len(skel_area)):									#Set size threshold to filter out noise and small areas unlikely to be part of network
				if skel_area[i].area >= 10: 										
					skel_area_filtered.append(skel_area[i].area)
			safnp = np.array(skel_area_filtered)								#Convert filtered skeleton areas (lengths) to numpy array
			skel_NPEX.append(safnp.sum())								#Append list with total sum of lengths
		skel_NPEX_array = np.array(skel_NPEX)
		skel_NPEX_avg.append(skel_NPEX_array.mean())	

	ttest = stats.ttest_ind(skel_control_avg, skel_NPEX_avg, equal_var = False)	#T-test between control and NPEX groups

	skel_plots = [skel_control_avg, skel_NPEX_avg]		#Plot boxplots for control vs. NPEX
	plt.subplot(3, 1, 2)
	plt.boxplot(skel_plots, patch_artist = True)
	plt.title("Skeleton length - NPEX vs. Control")
	plt.xlabel(ttest, color = "red")							#Print t-test results under boxplots
	plt.ylabel("Average total skeleton length")
	plt.xticks([1, 2], ["Control", "NPEX"])

def area(path_control, path_NPEX):
	area_control_avg = []
	area_NPEX_avg = []
	for path in control_paths:
		area_control = []
		for filename in glob.glob(os.path.join(path, "*.jpg")):
			img = ndimg.imread(filename)
			factin = img[:, :, 1]												#Green channel - f-actin
			thresh_local = filters.threshold_local(factin, block_size = 25)		#Adaptive/Local threshold
			factin_bin = thresh_local > 30										#Binarize based on local threshold

			area_count = measure.label(factin_bin, return_num = True)			#Count number of regions
			area_area = measure.regionprops(area_count[0])						#Calculate area of regions
			area_area_filtered = []												#Loop through list of regions and check size/area (in pixels)
			for i in range(0, len(area_area)):									#Set size threshold to filter out noise and small areas unlikely to be part of network
				if area_area[i].area >= 50: 										
					area_area_filtered.append(area_area[i].area)
			aafnp = np.array(area_area_filtered)								#Convert filtered areas to numpy array
			area_control.append(aafnp.sum())									#Append list with total sum of areas
		area_control_array = np.array(area_control)
		area_control_avg.append(area_control_array.mean())

	for path in NPEX_paths:
		area_NPEX = []
		for filename in glob.glob(os.path.join(path, "*.jpg")):
			img = ndimg.imread(filename)
			factin = img[:, :, 1]												#Green channel - f-actin
			thresh_local = filters.threshold_local(factin, block_size = 25)		#Adaptive/Local threshold
			factin_bin = thresh_local > 30										#Binarize based on local threshold						#Skeletonize from binary image

			area_count = measure.label(factin_bin, return_num = True)			#Count number of regions
			area_area = measure.regionprops(area_count[0])						#Calculate area of regions
			area_area_filtered = []												#Loop through list of regions and check size/area (in pixels)
			for i in range(0, len(area_area)):									#Set size threshold to filter out noise and small areas unlikely to be part of network
				if area_area[i].area >= 50: 										
					area_area_filtered.append(area_area[i].area)
			aafnp = np.array(area_area_filtered)								#Convert filtered areas to numpy array
			area_NPEX.append(aafnp.sum())									#Append list with total sum of areas	
		area_NPEX_array = np.array(area_NPEX)
		area_NPEX_avg.append(area_NPEX_array.mean())

	ttest_area = stats.ttest_ind(area_control_avg, area_NPEX_avg, equal_var = False)	#T-test between control and NPEX groups

	area_plots = [area_control_avg, area_NPEX_avg]				#Plot boxplots for control vs. NPEX
	plt.subplot(3, 1, 3)
	plt.boxplot(area_plots, patch_artist = True)
	plt.title("Total area - NPEX vs. Control")
	plt.xlabel(ttest_area, color = "red")							#Print t-test results under boxplots
	plt.ylabel("Average total area")
	plt.xticks([1, 2], ["Control", "NPEX"])
	plt.tight_layout()
	plt.savefig("CountSkelArea_Results.png")

cellcount(path_control, path_NPEX)
skeletonize(path_control, path_NPEX)
area(path_control, path_NPEX)