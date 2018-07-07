find ../newrawdata/* -type f -exec sed -i '/transition/d' {} +
find ../newrawdata/* -type f -exec sed -i '/Reading/d' {} +
find ../newrawdata/* -type f  -exec sed -i '/^\./d' {} +
find ../newrawdata/* -type f  -exec sed -i '/^$/d' {} +
