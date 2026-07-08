class Solution {
public:
    const int mod = 1e9 + 7;
    typedef long long ll;

    // Fast Binary Exponentiation: computes (a^b) % mod
    ll pow(ll a, ll b) {
        ll res = 1;
        while (b) {
            if (b & 1) res = res * a % mod;
            a = a * a % mod;
            b >>= 1;
        }
        return res;
    }

    vector<int> sumAndMultiply(string s, vector<vector<int>>& queries) {
        int n = s.size();

        // Prefix sum of non-zero digits
        vector<ll> prefSum(n, 0);

        // Prefix number formed by concatenating non-zero digits (mod MOD)
        vector<ll> prefNonZeroNum(n, 0);

        // Prefix count of non-zero digits
        vector<ll> prefNonZeroCnt(n, 0);

        // Build prefix arrays
        for (int i = 0; i < n; i++) {
            int digit = s[i] - '0';

            // Copy previous prefix values
            if (i) {
                prefSum[i] = prefSum[i - 1];
                prefNonZeroNum[i] = prefNonZeroNum[i - 1];
                prefNonZeroCnt[i] = prefNonZeroCnt[i - 1];
            }

            // Ignore zeros since they don't contribute
            if (digit) {
                // Update prefix digit sum
                prefSum[i] = (prefSum[i] + digit) % mod;

                // Increase count of non-zero digits
                prefNonZeroCnt[i]++;

                // Append current digit to the prefix number
                prefNonZeroNum[i] = (prefNonZeroNum[i] * 10 + digit) % mod;
            }
        }

        vector<int> ans;

        // Process each query independently
        for (auto &q : queries) {
            int l = q[0], r = q[1];

            // Sum of non-zero digits in the substring
            ll sum = prefSum[r] - (l ? prefSum[l - 1] : 0);
            sum = (sum % mod + mod) % mod;

            // Number of non-zero digits in the substring
            ll cnt = prefNonZeroCnt[r] - (l ? prefNonZeroCnt[l - 1] : 0);

            // Extract the concatenated non-zero number of the substring
            ll num = prefNonZeroNum[r] -
                     (l ? (prefNonZeroNum[l - 1] * pow(10, cnt)) % mod : 0);
            num = (num % mod + mod) % mod;

            // Required answer = number × digit sum
            ans.push_back((int)((sum * num) % mod));
        }

        return ans;
    }
};