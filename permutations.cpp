#include <bits/stdc++.h>

using namespace std;

void calculate_permutations(vector<int> v,
                            vector<vector<int>> &v_permutations) {
  if (v.empty()) {
    v_permutations.push_back(v);
    return;
  }

  int x = v.back();
  v.pop_back();

  vector<vector<int>> v_sub_permutations;
  calculate_permutations(v, v_sub_permutations);

  for (auto sub_permutation : v_sub_permutations) {
    for (int i = 0; i < sub_permutation.size(); i++) {
      vector<int> permutation;
      for (int k = 0; k < i; k++) {
        permutation.push_back(sub_permutation[k]);
      }
      permutation.push_back(x);
      for (int k = i; k < sub_permutation.size(); k++) {
        permutation.push_back(sub_permutation[k]);
      }
      v_permutations.push_back(permutation);
    }
    vector<int> permutation;
    for (int i = 0; i < sub_permutation.size(); i++) {
      permutation.push_back(sub_permutation[i]);
    }
    permutation.push_back(x);
    v_permutations.push_back(permutation);
  }
}

void test_1() {
  vector<int> v;
  vector<vector<int>> v_permutations;

  calculate_permutations(v, v_permutations);

  assert(v_permutations.size() == 1);
  assert(v_permutations[0].size() == 0);
}

void test_2() {
  int N = 3;
  vector<int> v;
  for (int i = 1; i <= N; i++) {
    v.push_back(i);
  }
  vector<vector<int>> v_permutations;

  calculate_permutations(v, v_permutations);

  for (auto permutation : v_permutations) {
    for (auto x : permutation) {
      cout << x << " ";
    }
    cout << endl;
  }
}

int main() {
  cout << "TEST 1" << endl;
  test_1();
  cout << "TEST 2" << endl;
  test_2();
  cout << "Done" << endl;
  return 0;
}
