# Import genetic indices
from genetic_indices import genetic_indices

# Load stabilometric signals:
import pandas as pd
copx = pd.read_csv('cop_data_demo\copx.csv').iloc[:, 0] # It should be a pandas.Series type
copy = pd.read_csv('cop_data_demo\copy.csv').iloc[:, 0] # It should be a pandas.Series type

#Initialize the genetic_indices class using some stabilometric signal:
genetic_cop = genetic_indices(CoPx=copx , CoPy=copy)

# Compute genetic center of pressure indices
genetic_distance_index = genetic_cop.distance()
genetic_area_index = genetic_cop.area()
genetic_hybrid_index = genetic_cop.hybrid()
genetic_frequency_index = genetic_cop.frequency()
genetic_entropy_index = genetic_cop.entropy()
genetic_fall_risk_index = genetic_cop.fall_risk()

# Display results
print("Genetic Center of Pressure Indices:")
print(f"  ➤ Distance Index      : {genetic_distance_index:.6f}")
print(f"  ➤ Area Index          : {genetic_area_index:.6f}")
print(f"  ➤ Hybrid Index        : {genetic_hybrid_index:.6f}")
print(f"  ➤ Frequency Index     : {genetic_frequency_index:.6f}")
print(f"  ➤ Entropy Index       : {genetic_entropy_index:.6f}")
print(f"  ➤ Fall Risk Index     : {genetic_fall_risk_index:.6f}")