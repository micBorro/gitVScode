import numpy as np
from PIL import Image
from matplotlib import pyplot as plt

# Ouvrir l'image et la convertir en niveaux de gris
img1 = Image.open("lenabw.png").convert('L')  # 'L' pour niveaux de gris
img2 = Image.open("lenabruité.png").convert('L')  # 'L' pour niveaux de gris

# Convertir en tableau numpy pour traitement
img_np = np.array(img1)
img_bruit= np.array(img2)

# Créer une copie pour y ajouter du bruit poivre et sel
salt_img = img_np.copy()
prob = 0.08 # proportion de pixels à altérer

# Générer une matrice de bruit aléatoire
rand = np.random.rand(*img_np.shape)

# Ajouter du sel (blanc)
salt_img[rand < (prob / 2)] = 255
# Ajouter du poivre (noir)
salt_img[rand > 1 - (prob / 2)] = 0

# Dimensions de la figure
plt.figure(figsize=(12, 6))

# Sous-graphe 1 : image originale
plt.subplot(1, 3, 1)
plt.title("Image originale en niveaux de gris")
plt.imshow(img_np, cmap='gray')
plt.axis('off')

# Sous-graphe 2 : image sel poivre
plt.subplot(1, 3, 2)
plt.title("Image avec Poivre et Sel")
plt.imshow(salt_img, cmap='gray')
plt.axis('off')

# Sous-graphe 3 : image bruitée
plt.subplot(1, 3, 3)
plt.title("Image avec bruit")
plt.imshow(img_bruit, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()
img1.filter