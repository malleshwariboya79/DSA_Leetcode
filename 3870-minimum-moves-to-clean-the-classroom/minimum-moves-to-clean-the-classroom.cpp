class Solution {
public:
    int minMoves(vector<string>& classroom, int energy) {
        int m = classroom.size();
        int n = classroom[0].size();

        vector<vector<int>> litterId(m, vector<int>(n, -1));

        int k = 0;
        int sr = 0;
        int sc = 0;

        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if (classroom[r][c] == 'S') {
                    sr = r;
                    sc = c;
                } else if (classroom[r][c] == 'L') {
                    litterId[r][c] = k++;
                }
            }
        }

        if (k == 0) {
            return 0;
        }

        int fullMask = (1 << k) - 1;

        vector<vector<vector<int>>> best(
            m,
            vector<vector<int>>(n, vector<int>(1 << k, -1))
        );

        queue<array<int, 5>> q;

        best[sr][sc][0] = energy;
        q.push({sr, sc, 0, energy, 0});

        int dirs[4][2] = {
            {-1, 0},
            {1, 0},
            {0, -1},
            {0, 1}
        };

        while (!q.empty()) {
            auto [r, c, mask, e, moves] = q.front();
            q.pop();

            for (auto& d : dirs) {
                int nr = r + d[0];
                int nc = c + d[1];

                if (nr < 0 || nr >= m || nc < 0 || nc >= n) {
                    continue;
                }

                if (classroom[nr][nc] == 'X') {
                    continue;
                }

                int ne = e - 1;

                if (ne < 0) {
                    continue;
                }

                int nmask = mask;

                if (classroom[nr][nc] == 'R') {
                    ne = energy;
                }

                if (classroom[nr][nc] == 'L') {
                    nmask |= 1 << litterId[nr][nc];
                }

                if (nmask == fullMask) {
                    return moves + 1;
                }

                if (ne <= best[nr][nc][nmask]) {
                    continue;
                }

                best[nr][nc][nmask] = ne;
                q.push({nr, nc, nmask, ne, moves + 1});
            }
        }

        return -1;
    }
};