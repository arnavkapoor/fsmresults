find . -type f -exec sed -i '/transition/d' {} +
find . -type f -exec sed -i '/Reading/d' {} +
find . -type f  -exec sed -i '/^\./d' {} +
find . -type f  -exec sed -i '/^$/d' {} +
