####### TEST OF MULTI PLOT FOR ALL ##########
import xarray as xr
import matplotlib.pyplot as plt # plotting tool 
from matplotlib import colors   # visualization tool, specifying colors for plotting 
import cartopy.crs as ccrs      # visualization tool, ploting maps
import cartopy.feature          # visualization tool, projection list in cartopy

ds = xr.open_dataset('MARv3.9-ACCESS13-2074.nc', decode_times=False)


season = input('Enter season [MAM,JJA,SON]:')
TAS = int(input('For season:MAM; Enter TAS =3\n For season:JJA,SON; Enter TAS=4\n Enter TAS='))

#CMIP5 models
ACCESS_rol_4 = xr.open_dataset('ACCESS_rol_'+str(TAS)+'_'+season+'.nc').mean(dim='year')
HADGEM_rol_4 = xr.open_dataset('HADGEM_rol_'+str(TAS)+'_'+season+'.nc').mean(dim='year')
HADGEM_cloud_rol_4 = xr.open_dataset('HADGEM_cloud_rol_'+str(TAS)+'_'+season+'.nc').mean(dim='year')
HADGEM_SMB_rol_4 = xr.open_dataset('HADGEM_SMB_rol_'+str(TAS)+'_'+season+'.nc').mean(dim='year')
CSIRO_rol_4  = xr.open_dataset('CSIRO_rol_'+str(TAS)+'_'+season+'.nc').mean(dim='year')
IPSL_rol_4   = xr.open_dataset('IPSL_rol_'+str(TAS)+'_'+season+'.nc').mean(dim='year')
MIROC5_rol_4 = xr.open_dataset('MIROC5_rol_'+str(TAS)+'_'+season+'.nc').mean(dim='year')
NORESM_rol_4 = xr.open_dataset('NORESM_rol_'+str(TAS)+'_'+season+'.nc').mean(dim='year')

#CMIP6 models
CESM_rol_4      = xr.open_dataset('CESM_rol_'+str(TAS)+'_'+season+'.nc').mean(dim='year')
CNRM_ESM2_rol_4 = xr.open_dataset('CNRM_ESM2_rol_'+str(TAS)+'_'+season+'.nc').mean(dim='year')
CNRM_CM6_rol_4  = xr.open_dataset('CNRM_CM6_rol_'+str(TAS)+'_'+season+'.nc').mean(dim='year')
MRI_rol_4       = xr.open_dataset('MRI_rol_'+str(TAS)+'_'+season+'.nc').mean(dim='year')
UKMO_rol_4      = xr.open_dataset('UKMO_rol_'+str(TAS)+'_'+season+'.nc').mean(dim='year')

ACCESS       = ACCESS_rol_4 
HADGEM       = HADGEM_rol_4 
HADGEM_cloud = HADGEM_cloud_rol_4
HADGEM_SMB   = HADGEM_SMB_rol_4 
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


for i in range(len(CMIP5_models)):
    CC_cmip5 = CMIP5_models[i].CC
    CC_CMIP5.append(CC_cmip5)
      
    CU_cmip5 = CMIP5_models[i].CU
    CU_CMIP5.append(CU_cmip5)
    
    CM_cmip5 = CMIP5_models[i].CM
    CM_CMIP5.append(CM_cmip5)
    
    CD_cmip5 = CMIP5_models[i].CD
    CD_CMIP5.append(CD_cmip5)


CC_CMIP5_model_mean = model_mean(CC_CMIP5)
CU_CMIP5_model_mean = model_mean(CU_CMIP5)
CM_CMIP5_model_mean = model_mean(CM_CMIP5)
CD_CMIP5_model_mean = model_mean(CD_CMIP5)

#CMIP6 models
CMIP6_models = [CESM, CNRM_ESM2, CNRM_CM6, MRI, UKMO]

CC_CMIP6 = [] #Cloud Cover (total)
CU_CMIP6 = [] #Cloud Cover (UP)
CM_CMIP6 = [] #Cloud COver (Middle)
CD_CMIP6 = [] #Cloud Cover (Down)


for i in range(len(CMIP6_models)):
    CC_cmip6 = CMIP6_models[i].CC
    CC_CMIP6.append(CC_cmip6)
    
    CU_cmip6 = CMIP6_models[i].CU
    CU_CMIP6.append(CU_cmip6)
    
    CM_cmip6 = CMIP6_models[i].CM
    CM_CMIP6.append(CM_cmip6)
    
    CD_cmip6 = CMIP6_models[i].CD
    CD_CMIP6.append(CD_cmip6)


CC_CMIP6_model_mean = model_mean(CC_CMIP6)
CU_CMIP6_model_mean = model_mean(CU_CMIP6)
CM_CMIP6_model_mean = model_mean(CM_CMIP6)
CD_CMIP6_model_mean = model_mean(CD_CMIP6)

# (CMIP6-CMIP5)
CC_diff = CC_CMIP6_model_mean - CC_CMIP5_model_mean
CU_diff = CU_CMIP6_model_mean - CU_CMIP5_model_mean
CM_diff = CM_CMIP6_model_mean - CM_CMIP5_model_mean
CD_diff = CD_CMIP6_model_mean - CD_CMIP5_model_mean

### ======= MULTIPLOT ======= ###
proj = ccrs.LambertConformal(central_longitude=-35,
                            central_latitude=65,
                            standard_parallels=[35])

fig, axes = plt.subplots( ncols=3, nrows=4, figsize=(10, 12), subplot_kw={'projection': proj})

ax = axes.ravel().tolist()


for i in [0,1,2,3,4,5,6,7,8,9,10,11]:
    ax[i].add_feature(cartopy.feature.OCEAN.with_scale(
        '50m'), zorder=1, facecolor='white')           
    ax[i].add_feature(cartopy.feature.COASTLINE.with_scale(
        '50m'), zorder=1, edgecolor='black')
    ax[i].set_extent([-58, -22, 59, 83.5], ccrs.PlateCarree())    


#divnorm=colors.TwoSlopeNorm(vmin=vmin, vcenter=vcenter, vmax=vmax)
#divnorm=colors(vmin=vmin, vcenter=vcenter, vmax=vmax)
    
#CMIP5 model mean
cont = ax[0].pcolormesh(ds['LON'], ds['LAT'], CC_CMIP5_model_mean*100,   
                                    transform=ccrs.PlateCarree(),
                                    cmap='RdBu_r', vmin= -8, vmax=8)
#CMIP6 model mean
cont2 = ax[1].pcolormesh(ds['LON'], ds['LAT'], CC_CMIP6_model_mean*100,   
                                    transform=ccrs.PlateCarree(),
                                    cmap='RdBu_r', vmin= -8, vmax=8)
#CMIP5 model mean
cont3 = ax[2].pcolormesh(ds['LON'], ds['LAT'], CC_diff*100,   
                                    transform=ccrs.PlateCarree(),
                                    cmap='RdBu_r', vmin= -8, vmax=8)
#CMIP6 model mean
cont4 = ax[3].pcolormesh(ds['LON'], ds['LAT'], CU_CMIP5_model_mean*100,   
                                    transform=ccrs.PlateCarree(),
                                    cmap='RdBu_r', vmin= -8, vmax=8)

#CMIP5 model mean
cont = ax[4].pcolormesh(ds['LON'], ds['LAT'], CU_CMIP6_model_mean*100,   
                                    transform=ccrs.PlateCarree(),
                                    cmap='RdBu_r', vmin= -8, vmax=8)
#CMIP6 model mean
cont2 = ax[5].pcolormesh(ds['LON'], ds['LAT'], CU_diff*100,   
                                    transform=ccrs.PlateCarree(),
                                    cmap='RdBu_r', vmin= -8, vmax=8)
#CMIP5 model mean
cont3 = ax[6].pcolormesh(ds['LON'], ds['LAT'], CM_CMIP5_model_mean*100,   
                                    transform=ccrs.PlateCarree(),
                                    cmap='RdBu_r', vmin= -8, vmax=8)
#CMIP6 model mean
cont4 = ax[7].pcolormesh(ds['LON'], ds['LAT'], CM_CMIP6_model_mean*100,   
                                    transform=ccrs.PlateCarree(),
                                    cmap='RdBu_r', vmin= -8, vmax=8)
#CMIP5 model mean
cont = ax[8].pcolormesh(ds['LON'], ds['LAT'], CM_diff*100,   
                                    transform=ccrs.PlateCarree(),
                                    cmap='RdBu_r', vmin= -8, vmax=8)
#CMIP5 model mean
cont3 = ax[9].pcolormesh(ds['LON'], ds['LAT'], CD_CMIP5_model_mean*100,   
                                    transform=ccrs.PlateCarree(),
                                    cmap='RdBu_r', vmin= -8, vmax=8)
#CMIP6 model mean
cont4 = ax[10].pcolormesh(ds['LON'], ds['LAT'], CD_CMIP6_model_mean*100,   
                                    transform=ccrs.PlateCarree(),
                                    cmap='RdBu_r', vmin= -8, vmax=8)
#CMIP6 model mean
cont4 = ax[11].pcolormesh(ds['LON'], ds['LAT'], CD_diff*100,   
                                    transform=ccrs.PlateCarree(),
                                    cmap='RdBu_r', vmin= -8, vmax=8)



    
plt.rcParams.update({
"text.usetex": True,
"font.family": 'DejaVu Sans',
"font.serif": ["Computer Modern Roman"],
"font.size": 20})

#Top title
title_top = ['CMIP5', 'CMIP6', '(CMIP6-CMIP5)']    
j = 0
for i in [0,1,2]:
    ax[i].set_title(title_top[j], fontsize=14)
    j += 1
    
# Left side title
title_left = ['Total', 'Upper\n level', 'Mid\n level', 'Lower\n level']    
j = 0
for i in [0, 3, 6, 9]:
    ax[i].text(-0.5, 0.5, title_left[j], transform=ax[i].transAxes,fontsize=14, fontweight="bold")
    j += 1
    

#ax[0,1].set_title(title_fig_l, fontsize= fontsize_title_fig)
#ax[0].set_fontname("Computer Modern Roman")
#ax[1,1].set_title(title_fig_r, fontsize= fontsize_title_fig)



#remove outer box of the plot 
fig.patch.set_visible(False)
ax[0].axis('off')
ax[1].axis('off')
ax[2].axis('off')
ax[3].axis('off')
ax[4].axis('off')
ax[5].axis('off')
ax[6].axis('off')
ax[7].axis('off')
ax[8].axis('off')
ax[9].axis('off')
ax[10].axis('off')
ax[11].axis('off')

fig.canvas.draw()
fig.tight_layout(pad=0.01)
fig.tight_layout(pad=0.01)
fig.tight_layout(pad=0.01)
fig.tight_layout(pad=0.01)
    

#plt.subplots_adjust(left=0.2, right=0.98, top=0.97, bottom=0.24)
plt.subplots_adjust(left=0.2, right=0.98, top=0.93, bottom=0.20)
cbar = fig.colorbar(cont2, ax=ax, shrink=0.7, orientation ='vertical')
cbar.set_label('MAR Cloud Cover amonalies [$\%$]', fontsize=20)


plt.suptitle(season, fontsize = 20, y=0.99,x=0.64)
plt.show()
    
#if savefig == True:
#fig.savefig('/projects/NS9600K/idunnam/Thesis/src/Figures/1_deg_spatial_plots/test_multiplot.png')
fig.savefig(str(TAS)+'_'+season+'_deg_Cloud_multiplot.pdf',bbox_inches='tight',dpi=300)
