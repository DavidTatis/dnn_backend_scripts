
# %%
# conda run -n env python -c "print('Hello!')"
import numpy as np
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten, Lambda, BatchNormalization
from tensorflow.keras.layers import Convolution2D, MaxPooling2D, AveragePooling2D, Input,concatenate
from tensorflow.keras.models import Model
from tensorflow.keras.callbacks import ModelCheckpoint,EarlyStopping
from tensorflow.keras.optimizers import SGD
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import KFold
from tensorflow.keras.utils import plot_model
import pandas as pd
from sklearn.utils import resample
from sklearn.model_selection import train_test_split
import pickle
import timeit
from operator import itemgetter
import sys
# %%

# Model
def create_new_model():
    input_vec = Input(shape=(86,))
    x0=Activation('relu')(BatchNormalization()(Dense(1024)(input_vec)))
    m1=concatenate([input_vec, x0], axis=-1)
    x1=Activation('relu')(BatchNormalization()(Dense(1024)(m1)))
    m2=concatenate([m1, x1], axis=-1)
    x2=Activation('relu')(BatchNormalization()(Dense(1024)(m2)))
    m3=concatenate([m2, x2], axis=-1)
    x3=Activation('relu')(BatchNormalization()(Dense(1024)(m3)))

    m4=concatenate([m3, x3], axis=-1)
    x4=Activation('relu')(BatchNormalization()(Dense(512)(m4)))
    m5=concatenate([m4, x4], axis=-1)
    x5=Activation('relu')(BatchNormalization()(Dense(512)(m5)))
    m6=concatenate([m5, x5], axis=-1)
    x6=Activation('relu')(BatchNormalization()(Dense(512)(m6)))


    m7=concatenate([m6, x6], axis=-1)
    x7=Activation('relu')(BatchNormalization()(Dense(256)(m7)))
    m8=concatenate([m7, x7], axis=-1)
    x8=Activation('relu')(BatchNormalization()(Dense(256)(m8)))
    m9=concatenate([m8, x8], axis=-1)
    x9=Activation('relu')(BatchNormalization()(Dense(256)(m9)))

    m10=concatenate([m9, x9], axis=-1)
    x10=Activation('relu')(BatchNormalization()(Dense(128)(m10)))
    m11=concatenate([m10, x10], axis=-1)
    x11=Activation('relu')(BatchNormalization()(Dense(128)(m11)))
    m12=concatenate([m11, x11], axis=-1)
    x12=Activation('relu')(BatchNormalization()(Dense(128)(m12)))

    m13=concatenate([m12, x12], axis=-1)
    x13=Activation('relu')(BatchNormalization()(Dense(64)(m13)))
    m14=concatenate([m13, x13], axis=-1)
    x14=Activation('relu')(BatchNormalization()(Dense(64)(m14)))

    m15=concatenate([m14, x14], axis=-1)
    x15=Activation('relu')(BatchNormalization()(Dense(32)(m15)))

    m16=concatenate([m15, x15], axis=-1)
    x16=Dense(1,activation='linear')(m16)

    model=Model(input_vec,x16)
    # model.summary()
    return model

elements = ["H","Li","Be","B","C","N","O","F","Na","Mg","Al",
			"Si","P","S","Cl","K","Ca","Sc","Ti","V","Cr","Mn",
			"Fe","Co","Ni","Cu","Zn","Ga","Ge","As","Se","Br","Kr",
			"Rb","Sr","Y","Zr","Nb","Mo","Tc","Ru","Rh","Pd","Ag",
			"Cd","In","Sn","Sb","Te","I","Xe","Cs","Ba","La","Ce",
			"Pr","Nd","Pm","Sm","Eu","Gd","Tb","Dy","Ho","Er","Tm",
			"Yb","Lu","Hf","Ta","W","Re","Os","Ir","Pt","Au","Hg",
			"Tl","Pb","Bi","Ac","Th","Pa","U","Np","Pu"]



# def predict_element(compound):
model=create_new_model()
model_path="/home/app_cawt/IRNET-0.4.h5"
model.load_weights(model_path)

compounds=(sys.argv[1]).replace("'","")
compounds=compounds.replace("[","")
compounds=compounds.replace("]","")
compounds=compounds.replace(" ","")

compounds=compounds.split(",")

try:

    values=(sys.argv[2]).replace("'","")
    values=values.replace("[","")
    values=values.replace("]","")
    values=values.replace(" ","")

    values=values.split(",")
    values=[int(v) for v in values]

    elementsToUse=compounds
    atoms=values
    elementsIndex=[elements.index(e) for e in elementsToUse]

    ratios = [0]*len(elements)

    for i in range(len(elementsIndex)):
        ratios[elementsIndex[i]]=round(atoms[i]/sum(atoms),3)

    predictions=list(model.predict(np.asarray([ratios])))
    print(predictions[0][0])
except ValueError:
    print("error")

    
# maxMol=10
# posibilities=[]
# population=[]
# formated={}
# byAtoms={}
# for x in range(1,2):
#     for y in range(1,2):
#         for z in range(1,2):

#             temp=[atoms[0]*x,
#                     atoms[1]*x,
#                     # end first compound
#                     atoms[2]*y,
#                     atoms[3]*y,
#                     atoms[4]*y,
#                     atoms[5]*y,
#                     # end second compound
#                     atoms[6]*z,
#                     atoms[7]*z
#                     # end third compound
#                     ]
            
#             ratios = [0]*len(elements)
            
#             formatedCompound=""
#             byAtomsCompound=""
#             for i in range(len(elementsIndex)):
#                 ratios[elementsIndex[i]]+=round(temp[i]/sum(temp),3)
                
                
#             totalAtoms=[round(atom/sum(temp),3) for atom in temp]
#             for i in range(len(elementsToUse)):
#                 formatedCompound+=elementsToUse[i]+str(totalAtoms[i])+", "
                
                

#             if(formatedCompound not in formated):
#                 population.insert(len(population),ratios)
#                 formated[formatedCompound]=len(population)-1 #save the index where is the compound  in the population
#                 byAtoms[f"x={x},y={y}, z={z}"]=len(population)-1 #save the index where is the compound  in the population




# print("total predictions: ",len(formated))

# model=create_new_model()
# model_path="/home/app_cawt/IRNET-0.4.h5"
# model.load_weights(model_path)

# predictions=list(model.predict(np.asarray(population)))

# sortIndex=sorted(range(len(predictions)), key=lambda k: predictions[k])
# print(sortIndex[0:5])

# print(f"{min(predictions)}:min prediction.  {max(predictions)}: max prediction.")

# for top in range (10):
# 	print(f"======Predicted as Top {top}======")
# 	print(predictions[sortIndex[top]])
# 	formatedValue = {i for i in formated if formated[i]==sortIndex[top]}
# 	byAtomsValue={i for i in byAtoms if byAtoms[i]==sortIndex[top]}
# 	print("by ratio: ",formatedValue)
# 	# print("by atoms: ",byAtomsValue)
# 	print(f"{min(predictions)} = {byAtomsValue}")



# # print(sortedIndex[0:10])
# # print(np.asarray(predictions)[0:10])
# # print("Eval. Population ",len(population))


# # %%

