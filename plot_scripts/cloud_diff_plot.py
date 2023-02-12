import xarray as xr
from function_diff_plot import diff_plot

season = input('Enter season here:')
#CMIP5 models
ACCESS_rol_4 = xr.open_dataset('ACCESS_rol_4_'+season+'.nc').mean(dim='year')
#HADGEM_rol_4 = xr.open_dataset('/HADGEM_rol_4'+season+'.nc').mean(dim='year')
HADGEM_cloud_rol_4 = xr.open_dataset('HADGEM_cloud_rol_4_'+season+'.nc').mean(dim='year')
#HADGEM_SMB_rol_4 = xr.open_dataset('HADGEM_SMB_rol_4_'+season+'.nc').mean(dim='year')
CSIRO_rol_4  = xr.open_dataset('CSIRO_rol_4_'+season+'.nc').mean(dim='year')
IPSL_rol_4   = xr.open_dataset('IPSL_rol_4_'+season+'.nc').mean(dim='year')
MIROC5_rol_4 = xr.open_dataset('MIROC5_rol_4_'+season+'.nc').mean(dim='year')
NORESM_rol_4 = xr.open_dataset('NORESM_rol_4_'+season+'.nc').mean(dim='year')

#CMIP6 models
CESM_rol_4      = xr.open_dataset('CESM_rol_4_'+season+'.nc').mean(dim='year')
CNRM_ESM2_rol_4 = xr.open_dataset('CNRM_ESM2_rol_4_'+season+'.nc').mean(dim='year')
CNRM_CM6_rol_4  = xr.open_dataset('CNRM_CM6_rol_4_'+season+'.nc').mean(dim='year')
MRI_rol_4       = xr.open_dataset('MRI_rol_4_'+season+'.nc').mean(dim='year')
UKMO_rol_4      = xr.open_dataset('UKMO_rol_4_'+season+'.nc').mean(dim='year')

ACCESS       = ACCESS_rol_4 
#HADGEM       = HADGEM_rol_4 
HADGEM_cloud = HADGEM_cloud_rol_4
#HADGEM_SMB   = HADGEM_SMB_rol_4 
CSIRO        = CSIRO_rol_4   
IPSL         = IPSL_rol_4   
MIROC5       = MIROC5_rol_4  
NORESM       = NORESM_rol_4  

#CMIP6 models
CESM      = CESM_rol_4       
CNRM_ESM2 = CNRM_ESM2_rol_4  
CNRM_CM6  = CNRM_CM6_rol_4   
MRI       = MRI_rol_4      
UKMO      = UKMO_rol_4     

#dataset for choosing coordinates
ds = xr.open_dataset('MARv3.9-ACCESS13-2074.nc', decode_times=False)

# === Calculate the model mean of each variable ==#
def model_mean(mod):
    return sum(mod)/ len(mod)


#CMIP5 models
CMIP5_models = [ACCESS, HADGEM_cloud, CSIRO, IPSL, MIROC5, NORESM]

CC_CMIP5 = [] #Cloud Cover (total)
CU_CMIP5 = [] #Cloud Cover (UP)
CM_CMIP5 = [] #Cloud COver (Middle)
CD_CMIP5 = [] #Cloud Cover (Down)
COD_CMIP5 = [] #Cloud Optical Depth


for i in range(len(CMIP5_models)):
    CC_cmip5 = CMIP5_models[i].CC
    CC_CMIP5.append(CC_cmip5)
      
    CU_cmip5 = CMIP5_models[i].CU
    CU_CMIP5.append(CU_cmip5)
    
    CM_cmip5 = CMIP5_models[i].CM
    CM_CMIP5.append(CM_cmip5)
    
    CD_cmip5 = CMIP5_models[i].CD
    CD_CMIP5.append(CD_cmip5)
    
    COD_cmip5 = CMIP5_models[i].COD
    COD_CMIP5.append(COD_cmip5)



CC_CMIP5_model_mean = model_mean(CC_CMIP5)
CU_CMIP5_model_mean = model_mean(CU_CMIP5)
CM_CMIP5_model_mean = model_mean(CM_CMIP5)
CD_CMIP5_model_mean = model_mean(CD_CMIP5)
COD_CMIP5_model_mean = model_mean(COD_CMIP5)


#CMIP6 models
CMIP6_models = [CESM, CNRM_ESM2, CNRM_CM6, MRI, UKMO]

CC_CMIP6 = [] #Cloud Cover (total)
CU_CMIP6 = [] #Cloud Cover (UP)
CM_CMIP6 = [] #Cloud COver (Middle)
CD_CMIP6 = [] #Cloud Cover (Down)
COD_CMIP6 = [] #Cloud Optical Depth


for i in range(len(CMIP6_models)):
    CC_cmip6 = CMIP6_models[i].CC
    CC_CMIP6.append(CC_cmip6)
    
    CU_cmip6 = CMIP6_models[i].CU
    CU_CMIP6.append(CU_cmip6)
    
    CM_cmip6 = CMIP6_models[i].CM
    CM_CMIP6.append(CM_cmip6)
    
    CD_cmip6 = CMIP6_models[i].CD
    CD_CMIP6.append(CD_cmip6)
    
    COD_cmip6 = CMIP6_models[i].COD
    COD_CMIP6.append(COD_cmip6)



CC_CMIP6_model_mean = model_mean(CC_CMIP6)
CU_CMIP6_model_mean = model_mean(CU_CMIP6)
CM_CMIP6_model_mean = model_mean(CM_CMIP6)
CD_CMIP6_model_mean = model_mean(CD_CMIP6)
COD_CMIP6_model_mean = model_mean(COD_CMIP6)


#===Tot Cloud Cover ===#
diff_plot(CC_CMIP6_model_mean*100,CC_CMIP5_model_mean*100, ds['LON'], ds['LAT'], 
          -8,8,
          surf_height_data = ds['SH'],
          add_contour_levels = True,
          contour_levels = [2000,3000],
          cbar_title='(CMIP6-CMIP5) tot. Cloud Cover anomalies [$\%$]',
          cmap_color='RdBu_r',
          title_plot = '(CMIP6-CMIP5) MAR simulation',
          file_title='4_deg_diff_CC')


#===Tot Upper Cover ===#
diff_plot(CU_CMIP6_model_mean*100,CU_CMIP5_model_mean*100, ds['LON'], ds['LAT'], 
          -8,8,
          surf_height_data = ds['SH'],
          add_contour_levels = True,
          contour_levels = [2000,3000],
          cbar_title='(CMIP6-CMIP5) High level Cloud Cover anomalies [$\%$]',
          cmap_color='RdBu_r',
          title_plot = '(CMIP6-CMIP5) MAR simulation',
          file_title='4_deg_diff_CU')

#===Tot Middle Cover ===#
diff_plot(CM_CMIP6_model_mean*100,CM_CMIP5_model_mean*100, ds['LON'], ds['LAT'],
          -8,8,
          surf_height_data = ds['SH'],
          add_contour_levels = True,
          contour_levels = [2000,3000],
          cbar_title='(CMIP6-CMIP5) Mid level Cloud Cover anomalies [$\%$]',
          cmap_color='RdBu_r',
          title_plot = '(CMIP6-CMIP5) MAR simulation',
          file_title='4_deg_diff_CM')

#===Tot Lower Cover ===#
diff_plot(CD_CMIP6_model_mean*100,CD_CMIP5_model_mean*100, ds['LON'], ds['LAT'], 
          -8,8,
          surf_height_data = ds['SH'],
          add_contour_levels = True,
          contour_levels = [2000,3000],
          cbar_title='(CMIP6-CMIP5) Low level Cloud Cover anomalies [$\%$]',
          cmap_color='RdBu_r',
          title_plot = '(CMIP6-CMIP5) MAR simulation',
          file_title='4_deg_diff_CD')

#===Cloud optical depth ===#
diff_plot(COD_CMIP6_model_mean,COD_CMIP5_model_mean, ds['LON'], ds['LAT'], 
          -1,1,
          surf_height_data = ds['SH'],
          add_contour_levels = True,
          contour_levels = [2000,3000],
          cbar_title='(CMIP6-CMIP5) Cloud Optical Depth anomalies',
          cmap_color='RdBu_r',
          title_plot = '(CMIP6-CMIP5) MAR simulation',
          file_title='4_deg_diff_COD')




