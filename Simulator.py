class QuantumCircuit:
    
    
    I=[[1,0],[0,1]]
    
    
    zero_vector=[[1],[0]]
    
    
    job=[]
    
    
    def __init__(self,no_of_qubits):
        
       
        self.no_of_qubits=no_of_qubits
        
        
        basis=[]
        
        
        mat= [[1]]
        
        
        state_vector=[[1]]
        
        for i in range(self.no_of_qubits):
            mat=self.Tensor_matrix(mat,self.I)
            state_vector=self.Tensor_matrix(state_vector,self.zero_vector)
            
        self.unitary=mat
        self.state_vector=state_vector
        
        for i in range(2**self.no_of_qubits):
            basis.append(self.basis_state(i))
        self.basis=basis
        
    def pow(self,a,b):
        x=1
        for i in range(1,b+1):
            x = x*a
        return x
    
    def sin(self,b):
        s = b - (b**3)/(6) + (b**5)/(120) - (b**7)/(5040) + (b**9)/(362880)
        return s
    
    
    def cos(self,a):
        c = 1 - (a**2)/(2) + (a**4)/(24) - (a**6)/(720) + (a**8)/(40320)
        return c
    
    def tan(self,a):
        t = sin(a)/cos(a)
        return t 
        
    
    def basis_state(self,n):
        a=[]
        if n>0:
            while(n>0):
                dig=n%2
                a.append(dig)
                n=n//2
        else:
            a=[0]
        a.reverse()
        while(len(a)!=self.no_of_qubits):
            a=[0]+a
        str_=''
        for i in a:
            str_+=str(i)
        return str_
    
    def createMatrix(self,n):
        mat = []
        for i in range(n):
            rowList = []
            for j in range(n):
                rowList.append(0)
            mat.append(rowList)

        return mat
    
    def sqrt(self,n):
        return n**(1/2)
    
    def binaryToDecimal(self,binary):
     
        binary1 = binary
        decimal, i, n = 0, 0, 0
        while(binary != 0):
            dec = binary % 10
            decimal = decimal + dec * pow(2, i)
            binary = binary//10
            i += 1
        return decimal
    
    
    def vector_mat_mul(self,v,G):
        result=[]
        for i in range(len(G[0])):
            total=0
            for j in range(len(v)):
                total+= v[j][0]*G[i][j]
            result.append([total])
        return result
    
    
    def mat_mat_mul(self,mat1,mat2):
        res = [[0 for x in range(len(mat2[0]))] for y in range(len(mat1))]  
  
     
        for i in range(len(mat1)): 
            for j in range(len(mat2[0])): 
                for k in range(len(mat2)): 

                    
                    res[i][j] += mat1[i][k] * mat2[k][j] 
        return res
    
    
    
    def Tensor_vector(self, A, B):
        rowa=len(A)
        rowb=len(B)
        C = [[0] for i in range(rowa * rowb)]

        
        for i in range(0, rowa):

            
            for j in range(0, rowb):
                
                C[2*i + j][0] = A[i][0]* B[j][0]
                    
        return C 
    
    
    
    
    def Tensor_matrix(self, A , B ):
        if type(A[0])==int:
            cola=0
        else:
            cola = len(A[0])
        rowa = len(A)
        if type(B[0])==int:
            colb=0
        else:
            colb = len(B[0])
        rowb = len(B)

        C = [[0 for j in range(cola * colb)] for i in range(rowa * rowb)]
        
        
        for i in range(0, rowa):

            
            for j in range(0, cola):

                
                for k in range(0, rowb):

                    
                    for l in range(0, colb):

                        
                        C[2*i + k][2*j + l] = A[i][j] * B[k][l]
                       
        return C 
    
    
    
    def h(self,qubit_index):
        H_operator=[[1/self.sqrt(2),1/self.sqrt(2)],[1/self.sqrt(2),-1/self.sqrt(2)]]
        pdt=[[1]]
        for i in range(self.no_of_qubits-1,-1,-1):
            
            if i!=qubit_index:
                pdt= self.Tensor_matrix(pdt,self.I)
            else:
                pdt=self.Tensor_matrix(pdt,H_operator)
        self.unitary = self.mat_mat_mul(pdt,self.unitary)
        
        return 0
    
        
    
    
    def x(self,qubit_index):
        x_operator=[[0,1],[1,0]]
        pdt=[[1]]
        for i in range(self.no_of_qubits-1,-1,-1):
            
            if i!=qubit_index:
                pdt= self.Tensor_matrix(pdt,self.I)
            else:
                pdt=self.Tensor_matrix(pdt,x_operator)
        self.unitary = self.mat_mat_mul(pdt,self.unitary)
        
        return 0
        
    
    def z(self,qubit_index):
        z_operator=[[1,0],[0,-1]]
        pdt=[[1]]
        for i in range(self.no_of_qubits-1,-1,-1):
            
            if i!=qubit_index:
                pdt= self.Tensor_matrix(pdt,self.I)
            else:
                pdt=self.Tensor_matrix(pdt,z_operator)
        self.unitary = self.mat_mat_mul(pdt,self.unitary)
        
        return 0
        
    
    
    def r(self,angle,qubit_index):
        operator=[[self.cos(angle), -(self.sin(angle))],[self.sin(angle),self.cos(angle)]]
        pdt=[[1]]
        for i in range(self.no_of_qubits-1,-1,-1):
            
            if i!=qubit_index:
                pdt= self.Tensor_matrix(pdt,self.I)
            else:
                pdt=self.Tensor_matrix(pdt,operator)
        self.unitary = self.mat_mat_mul(pdt,self.unitary)
        
        return 0   
    

    
    def cx(self, control, target):
        cx_mat=self.createMatrix(2**self.no_of_qubits)
        for i in range(2**self.no_of_qubits):
            binary=(self.basis_state(i))[::-1]
            if binary[control]=='1':
                if binary[target]=='0':
                    binary=binary[:target]+'1'+binary[target+1:]
                else:
                    binary=binary[:target]+'0'+binary[target+1:]
            dec= self.binaryToDecimal(int(binary[::-1]))
            cx_mat[i][dec]=1
        self.unitary = self.mat_mat_mul(cx_mat,self.unitary)
        
        return 0
    
    def cz(self, control, target):
        self.h(target)
        self.cx(control, target)
        self.h(target)
        
        return 0
    
    def cr(self,angle,control,target):
        cr_mat=self.createMatrix(2**self.no_of_qubits)
        cr_operator=[[self.cos(angle), -self.sin(angle)],[self.sin(angle),self.cos(angle)]]
        for i in range(2**self.no_of_qubits):
            binary=(self.basis_state(i))[::-1]
            if binary[control]=='1':
                if binary[target]=='0':
                    dec_0= self.binaryToDecimal(int(binary[::-1]))
                    binary=binary[:target]+'1'+binary[target+1:]
                    dec_1= self.binaryToDecimal(int(binary[::-1]))
                    cr_mat[dec_0][i]=cr_operator[0][0]
                    cr_mat[dec_1][i]=cr_operator[1][0]
                else:
                    dec_1 = self.binaryToDecimal(int(binary[::-1]))
                    binary = binary[:target]+'0'+binary[target+1:]
                    dec_0 = self.binaryToDecimal(int(binary[::-1]))
                    cr_mat[dec_0][i]=cr_operator[0][1]
                    cr_mat[dec_1][i]=cr_operator[1][1]
            else:
                dec= self.binaryToDecimal(int(binary[::-1]))
                cr_mat[i][dec]=1
        self.unitary = self.mat_mat_mul(cr_mat,self.unitary)
        
        return 0
    
    def ccx(self,control1,control2,target):
        ccx_mat=self.createMatrix(2**self.no_of_qubits)
        for i in range(2**self.no_of_qubits):
            binary=(self.basis_state(i))[::-1]
            if binary[control1]=='1' and binary[control2]=='1':
                if binary[target]=='0':
                    binary=binary[:target]+'1'+binary[target+1:]
                else:
                    binary=binary[:target]+'0'+binary[target+1:]
            dec= self.binaryToDecimal(int(binary[::-1]))
            ccx_mat[i][dec]=1
        self.unitary = self.mat_mat_mul(ccx_mat,self.unitary)
        
        return 0
            

    
    def read_unitary(self):
        return self.unitary
        
        
    
    
    def read_state(self):
        self.state_vector=self.vector_mat_mul(self.state_vector,self.unitary)
        return self.state_vector
        
    
    
    
    def observing_probabilities(self):
        self.state_vector=self.vector_mat_mul(self.state_vector,self.unitary)
        prob={}
        for i in range(int(self.pow(2,self.no_of_qubits))):
            prob[self.basis[i]]=round((self.state_vector[i][0])**2,3)*100
        
        x=list(prob.keys())
        y=list(prob.values())
        return x,y
    def execute(self, the_number_of_shots=1024):
        result={}
        self.state_vector=self.vector_mat_mul(self.state_vector,self.unitary)
        for i in range(int(self.pow(2,self.no_of_qubits))):
            if self.state_vector[i][0]!=0:
                result[self.basis[i]]=round((self.state_vector[i][0])**2,3)*the_number_of_shots
        return result
