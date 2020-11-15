#include <stdio.h>
#include <stdlib.h>

int main(void) {
	long int m = 998244353; 
	
		int gcd(int a, int b) 
	{ 
	    if (a == 0) 
	        return b; 
	    return gcd(b % a, a); 
	} 
  
	long int modexp(long int x, long int n) 
	{ 
	    if (n == 0) { 
	        return 1; 
	    } 
	    else if (n % 2 == 0) { 
	        return modexp((x * x) % m, n / 2); 
	    } 
	    else { 
	        return (x * modexp((x * x) % m, (n - 1) / 2) % m); 
	    } 
	} 
  
	// Function to return the fraction modulo mod 
	long int getFractionModulo(long int a, long int b) 
	{ 
	    long int c = gcd(a, b); 
	  
	    a = a / c; 
	    b = b / c; 
	  
	    // (b ^ m-2) % m 
	    long int d = modexp(b, m - 2); 
	  
	    // Final answer 
	    long int ans = ((a % m) * (d % m)) % m; 
	  
	    return ans; 
	} 
	//Value of Q
	int get_total(int N, int rotations[]) {
		int total = 1; 
		for(int i = 0; i < N; i++){
			total *= rotations[i]; 
		}
		return total;
	}
	//Value of P
	int get_min_counts(int N, int rotations[]){
		int min_element = rotations[0]; 
		for(int i = 0; i < N; i++){
			if(rotations[i] < min_element){
				min_element = rotations[i]; 
			}
		}
		int start_from = (min_element - 1) / 2; 
		
		int prefix_count[N]; 
		for(int i = 0; i < N; i++){
				int uptil = 2 * start_from;
				int down = rotations[i] - uptil; 
				prefix_count[i] = down; 
		}
	
		
		int possible_combs_start = 1; 
		for(int i = 0; i < N; i++){
			possible_combs_start *= prefix_count[i]; 
		}
		
		int min_counts = possible_combs_start * start_from; 
		
		int i = 0; 

		// int res = 0; 
		int prev_combs = possible_combs_start; 
		for(int j = start_from; j > 0; j--){
			int possible_combs = 1; 
			for(int k = 0; k < N; k++){
				int contribution = prefix_count[k] + i * 2; 
				possible_combs *= contribution; 
			}
			min_counts += (possible_combs - prev_combs) * j; 
			prev_combs = possible_combs; 
			i++; 
		}
		
		return min_counts; 
	}
	
	long int get_result(int N, int rotations[]) { 
		int P = get_min_counts(N, rotations); 
		int Q = get_total(N, rotations); 
		Q = Q % m; 
		// printf("%d %d", P, Q); 
		long int res = getFractionModulo(P, Q);
		return res;
	}
	
	// READ INPUT
	int num_testcases = 1000; 
	// scanf("%d", &num_testcases); 
	for(int test = 0; test < num_testcases; test++){
		int N = 2500; 
		// scanf("%d", &N); 
		int rotations[N]; 
		for(int i = 0; i < N; i++){
			rotations[i] = rand() % 5000; 
			print("rotation [%d] : %d", i, rotations[i]); 
		}
		for(int i = 0; i < N; i++){
			int x; 
			scanf("%d", &x);
			rotations[i] = x + 1; 
		}
		long int res; 
		res = get_result(N, rotations); 
		printf("%ld%c", res, '\n'); 
	}
	return 0;
}
