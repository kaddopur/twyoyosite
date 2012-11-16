watch('.*\.coffee') {|md| system("coffee -bc -o ..\\js #{md[0]}")}
# Produce ugly HTML
# watch('.*\.jade')   {|md| system("jade -O .. .")}
watch('.*\.jade')   {|md| system("jade -P -O .. .")}
watch('.*\.styl')   {|md| system("stylus -o ..\\css #{md[0]}")}

