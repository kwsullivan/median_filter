# median filtering
## program description
The following program will use median filtering to remove undesired moving objects from a series of photographs to retrieve the background image.<br>
A significant improvement to the algorithm is the implementation of algignment to the sequence of images before the sequence is processed through median filtering to produce significantly improved results.<br>
The program also utilizes various post-processing techniques to improve the output for potential consumer application of the program.

## summary of test images
| series name | degree of camera shake | degree of overlap | number of frames |
| --------- | ----------------- | -------------- | ------------- |
| android | very little | some overlap | 5 |
| cat | severe | severe | 6 |
| coffee_few | very little | none | 5 |
| coffee | very little | some overlap | 13 |
| drink_shake | severe | none | 3 |
| glasses | very little | none | 3 |
| phone | none | some | 6 |
| zoom | some | severe | 6 |
| kirby | severe | none | 6 |
| tiger | none | none | 6 |
| bottle | none | severe | 6 |
| mccafe | severe | severe | 6 |
| donald_level1 | none | none | 6 |
| donald_level2 | none | some overlap | 6 |
| donald_level3 | none | some overlap | 12 |
| wallet | some | some overlap | 5 |

Note: there are additional frames for kirby, tiger, and mccafe