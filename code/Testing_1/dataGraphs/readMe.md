# Interpreting the graphs

* The graphs(pdfs) generated are numbered based on the tanks - i.e. importantfeatures0 represent tank 0's graph
 - i.e. tank 0 is being made the target value, and its dependencies (or more imp features/tank flowrates) on the other tanks are calculated
* Residual graphs are not important - just gives an overview of the error clustering
* Due to the use of plot function for both residual graphs and impfeatures graph at the same time, some impfeatures graphs are overlapped with the residual graphs
* The colored horizontal lines are of prime interest, not the blue scattered points. Lines with positive extension, i.e. extending ahead of zero(towards right)
  is an important factor(feature, in this case 'dependency factor')
