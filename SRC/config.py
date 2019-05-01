#!/usr/bin/env python

"""
This script is used to store all configuration parameter to run the main code (jupyter notebook)

"""

import os

# Initialize dictionnaries
config_parameters = {}
data = {}


## Please update the following paths according to your own configuration 
config_parameters['GISBASE'] = '/usr/lib/grass76'
config_parameters['PYTHONLIB'] = '/usr/lib/python2.7'
config_parameters['locationepsg'] = '31370' #  EPSG code for Belgian Lambert 1972
config_parameters['njobs'] = 6

## The following parameters should not be changed normally
config_parameters['gisdb'] = '../../GRASSDATA' # path to GRASSDATA folder
config_parameters['permanent_mapset'] = 'PERMANENT' # name of the permanent mapset
config_parameters['outputfolder'] = '../../../Results'
config_parameters['location'] = "WALOUS_31370"

## Other folder for automatic output
config_parameters['outputfolder_Logfile'] = os.path.join(config_parameters['outputfolder'],"Log_file")
config_parameters['outputfolder_classfeatures'] = os.path.join(config_parameters['outputfolder'],"Classification_features")
config_parameters['outputfolder_training_sample'] = os.path.join(config_parameters['outputfolder'],"Training_sample")
config_parameters['outputfolder_classifRF'] = os.path.join(config_parameters['outputfolder'],"Classif_RF")
config_parameters['outputfolder_classifRF_tiles'] = os.path.join(config_parameters['outputfolder_classifRF'],"classif_tiles")

## Other path 
config_parameters['list_tiles'] = os.path.join(config_parameters['outputfolder'],"list_tiles")
config_parameters['pixel_classes_list'] = os.path.join(config_parameters['outputfolder'],"pixel_classes_list")
config_parameters['rf_trained_model'] = os.path.join(config_parameters['outputfolder_classifRF'],"rf_trained_model.rda")

## The following path linking to datasets should be changed according to your own folder organization 
data['tiles'] = ('tiles','/media/tais/data/WALOUS/Data/obia_2018/tuiles.gpkg') # Processing tiles (from OBIA processing)
data['training_points'] = ('training','../../../Data/points_fusion_all/points_fusion_all.shp')
data['obia_folder'] = '../../../Data/obia_2018'
#data['ortho_lc'] = ('ortho_lc','../../../Data/pixel_2018/walous_pixelbassed_2016_raw.tif') # 1 m res.
data['ortho_lc'] = ('ortho_lc','../../../Data/pixel_2018') # 1 m res.
data['senti_lc'] = ('sent_lc','../../../Data/pixel_2018/Walous_LC2018_RF_recoded.tif.tif') # 10 m res.
data['senti_croptype'] = ('senti_croptype','../../../Data/CropType/crop2016_type_31370.tif') # 10 m res.
data['binary_crop'] = ('binary_crop','../../../Data/CropType/crop2016_cm_31370.tif') # 10 m res.
data['binary_agri'] = ('SIGEC','../../../Data/SIGEC2017/SIGEC2017_mask_31370.tif') # 10 m res.
data['binary_forest'] = ('forest','../../../Data/masque_forestier/masque_forest_31370.tif') # 2 m res.
data['binary_hydro'] = ('hydro','../../../Data/squelette_vectoriel/Hydro_mask_31370.tif') # 2 m res.
data['binary_roadnet'] = ('roadnet','../../../Data/squelette_vectoriel/Roadnet_mask_31370.tif') # 2 m res.
data['binary_built'] = ('built','../../../Data/squelette_vectoriel/Buildings_mask_31370.tif') # 1 m res.

## Color rule file
data['color_file'] = "/media/tais/data/WALOUS/Data/fusion_colors.txt"