from sklearn.metrics import f1_score, precision_score, recall_score, precision_recall_curve
import numpy as np
from pprint import pprint

ucfcvd_gt = '/storage/users/multicog/Adit/UCFC-VD_Data_Prep/Files/ucfc-vd_tag_gt.npy'

ucfcvd_tag_feats = ['/storage/users/multicog/Adit/UCFC-VD_Tagging/ucfcvd_e100_tag_feats.npy',
                    '/storage/users/multicog/Adit/UCFC-VD_Tagging/ucfcvd_e200_tag_feats.npy',
                    '/storage/users/multicog/Adit/UCFC-VD_Tagging/ucfcvd_e400_tag_feats.npy',
                    '/storage/users/multicog/Adit/UCFC-VD_Tagging/ucfcvd_e800_tag_feats.npy',
                    '/storage/users/multicog/Adit/UCFC-VD_Tagging/ucfcvd_e1000_tag_feats.npy']

ucfcvd_res = {}
label = np.load(ucfcvd_gt)
for mfeat in ucfcvd_tag_feats:
    pred = np.load(mfeat)
    ap_list = []
    for j in range(pred.shape[1]):
        precision, recall, thresholds = precision_recall_curve(label[:,j], pred[:,j])
        ap = np.mean(precision)
        ap_list.append(ap)
    count = int(mfeat.split('_')[2][1:])
    ucfcvd_res[count] = np.mean(ap_list)

print('UCFC-VD results:')
pprint(ucfcvd_res)
