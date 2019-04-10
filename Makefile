PROGRAM=median.py
TEST=compare.py
PROCESS=crop.py

ifeq ($(OS),Windows_NT)
	COMPILER=py
	OPEN=
	OSFLAG += WIN
else
	COMPILER=python3
	OPEN=open
	OSFLAG += OSX
endif

# Median Filtering

filter: android bottle car cat coffee_few glasses kirby mccafe phone tiger zoom
#  Sequence Path - Aligned Path - Output Name - Post Processed Output Name
android: 
	$(COMPILER) $(PROGRAM) ./image_sequences/android/ ./image_sequences/aligned/android/ ./results/median_filter/android.jpg ./results/post_processed/android_post.jpg align=true
bottle: 
	$(COMPILER) $(PROGRAM) ./image_sequences/bottle/ ./image_sequences/aligned/bottle/ ./results/median_filter/bottle.jpg ./results/post_processed/bottle_post.jpg align=true
car: 
	$(COMPILER) $(PROGRAM) ./image_sequences/car/ ./image_sequences/aligned/car/ ./results/median_filter/car.jpg ./results/post_processed/car_post.jpg align=true
cat: 
	$(COMPILER) $(PROGRAM) ./image_sequences/cat/ ./image_sequences/aligned/cat/ ./results/median_filter/cat.jpg ./results/post_processed/cat_post.jpg align=true
coffee_few: 
	$(COMPILER) $(PROGRAM) ./image_sequences/coffee_few/ ./image_sequences/aligned/coffee_few/ ./results/median_filter/coffee_few.jpg ./results/post_processed/coffee_few_post.jpg align=true
coffee_large: 
	$(COMPILER) $(PROGRAM) ./image_sequences/coffee_large/ ./image_sequences/aligned/coffee_large/ ./results/median_filter/coffee_large.jpg ./results/post_processed/coffee_large_post.jpg align=true

glasses: 
	$(COMPILER) $(PROGRAM) ./image_sequences/glasses/ ./image_sequences/aligned/glasses/ ./results/median_filter/glasses.jpg ./results/post_processed/glasses_post.jpg align=true
kirby: 
	$(COMPILER) $(PROGRAM) ./image_sequences/kirby/ ./image_sequences/aligned/kirby/ ./results/median_filter/kirby.jpg ./results/post_processed/kirby_post.jpg align=true
mccafe: 
	$(COMPILER) $(PROGRAM) ./image_sequences/mccafe/ ./image_sequences/aligned/mccafe/ ./results/median_filter/mccafe.jpg ./results/post_processed/mccafe_post.jpg align=true
phone: 
	$(COMPILER) $(PROGRAM) ./image_sequences/phone/ ./image_sequences/aligned/phone/ ./results/median_filter/phone.jpg ./results/post_processed/phone_post.jpg align=true
tiger: 
	$(COMPILER) $(PROGRAM) ./image_sequences/tiger/ ./image_sequences/aligned/tiger/ ./results/median_filter/tiger.jpg ./results/post_processed/tiger_post.jpg  align=true
zoom: 
	$(COMPILER) $(PROGRAM) ./image_sequences/zoom/ ./image_sequences/aligned/zoom/ ./results/median_filter/zoom.jpg ./results/post_processed/zoom_post.jpg align=true

donald_level1:
	$(COMPILER) $(PROGRAM) ./image_sequences/donald_level1/ ./image_sequences/aligned/donald_level1/ ./results/median_filter/donald_level1.jpg ./results/post_processed/donald_level1_post.jpg align=false
donald_level2:
	$(COMPILER) $(PROGRAM) ./image_sequences/donald_level2/ ./image_sequences/aligned/donald_level2/ ./results/median_filter/donald_level2.jpg ./results/post_processed/donald_level2_post.jpg align=false
donald_level3:
	$(COMPILER) $(PROGRAM) ./image_sequences/donald_level3/ ./image_sequences/aligned/donald_level3/ ./results/median_filter/donald_level3.jpg ./results/post_processed/donald_level3_post.jpg align=false
wallet:
	$(COMPILER) $(PROGRAM) ./image_sequences/wallet/ ./image_sequences/aligned/wallet/ ./results/median_filter/wallet.jpg ./results/post_processed/wallet_post.jpg align=true

shaky_desk6:
	$(COMPILER) $(PROGRAM) ./image_sequences/shaky_desk6/ ./image_sequences/aligned/shaky_desk6/ ./results/median_filter/shaky_desk6.jpg ./results/post_processed/shaky_desk6_post.jpg align=true
shaky_desk12:
	$(COMPILER) $(PROGRAM) ./image_sequences/shaky_desk12/ ./image_sequences/aligned/shaky_desk12/ ./results/median_filter/shaky_desk12.jpg ./results/post_processed/shaky_desk12_post.jpg align=true
tim6:
	$(COMPILER) $(PROGRAM) ./image_sequences/tim6/ ./image_sequences/aligned/tim6/ ./results/median_filter/tim6.jpg ./results/post_processed/tim6_post.jpg align=true
tim12:
	$(COMPILER) $(PROGRAM) ./image_sequences/tim12/ ./image_sequences/aligned/tim12/ ./results/median_filter/tim12.jpg ./results/post_processed/tim12_post.jpg align=true


# Post Processing
post_wallet:
	$(COMPILER) $(PROCESS) ./results/median_filter/wallet.jpg ./results/post_processed/wallet_post.jpg
post_tim12:
	$(COMPILER) $(PROCESS) ./results/median_filter/tim12.jpg ./results/post_processed/tim12_post.jpg


# Difference Testing

tests: test_donald_level1 test_donald_level2 test_donald_level3 test_wallet test_wallet_crop

test_donald_level1:
	$(COMPILER) $(TEST) ./ground_truths/landscape.jpg ./results/median_filter/donald_level1.jpg 50
test_donald_level2:
	$(COMPILER) $(TEST) ./ground_truths/landscape.jpg ./results/median_filter/donald_level2.jpg 50
test_donald_level3:
	$(COMPILER) $(TEST) ./ground_truths/landscape.jpg ./results/median_filter/donald_level3.jpg 50

test_wallet_crop:
	$(COMPILER) $(TEST) ./ground_truths/desk_cropped.jpg ./results/median_filter/wallet_cropped.jpg 50

test_shaky_desk6:
	$(COMPILER) $(TEST) ./ground_truths/shaky_desk6_cropped.jpg ./results/median_filter/shaky_desk6_cropped.jpg 50
test_shaky_desk12:
	$(COMPILER) $(TEST) ./ground_truths/shaky_desk12_cropped.jpg ./results/median_filter/shaky_desk12_cropped.jpg 50

test_tim6:
	$(COMPILER) $(TEST) ./ground_truths/tim6_cropped.jpg ./results/median_filter/tim6_cropped.jpg 30
test_tim12:
	$(COMPILER) $(TEST) ./ground_truths/tim12_cropped.jpg ./results/median_filter/tim12_cropped.jpg 30