/*class Solution1 {
    public void setZeroes(int[][] matrix) {
        int rows=matrix.length;
        int cols=matrix[0].length;
        for(int i=0;i<rows;i++){
            for(int j=0;j<cols;j++){
                if(matrix[i][j]==0){
                    for(int k=0;k<rows;k++){
                        if(matrix[k][j]!=0){
                            matrix[k][j]=-2;
                        }
                    }
                    for(int k=0;k<cols;k++){
                        if(matrix[i][k]!=0){
                            matrix[i][k]=-2;
                        }
                    }
                }
            } 
        }
        for(int a=0;a<rows;a++){
            for(int b=0;b<cols;b++){
                if(matrix[a][b]==-2){
                    matrix[a][b]=0;
                }
            }
        }        
    }
}*/
class Solution{
    public void setZeroes(int [][] matrix){
        int rows=matrix.length;
        int cols=matrix[0].length;
        int[] m_cols=new int[cols];
        int[] m_rows=new int[rows];
        for(int i=0;i<rows;i++){
            for(int j=0;j<cols;j++){
                if(matrix[i][j]==0){
                    m_rows[i]=1;
                    m_cols[j]=1;
                }
            }
        }
        for(int a=0;a<rows;a++){
            for(int b=0;b<cols;b++){
                if(m_rows[a]==1 || m_cols[b]==1){
                    matrix[a][b]=0;
                }
            }
        }
        return;
    }
}