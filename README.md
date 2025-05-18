# 8-Puzzle Solver with AI Algorithms 🧩

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/Tkinter-GUI-blue?style=flat-square)
![License](https://img.shields.io/badge/license-MIT-green?style=flat-square)
![Visitor Count](https://visitor-badge.laobi.icu/badge?page_id=tai-dang.8puzzle-solver)

Đây là một dự án toàn diện triển khai các thuật toán AI để giải bài toán 8-Puzzle, tích hợp giao diện đồ họa (GUI) bằng Tkinter để minh họa quá trình giải. Dự án được thực hiện trong khuôn khổ môn Nhập môn Trí tuệ Nhân tạo tại HCMUTE.

---

## 🚀 Tổng quan dự án

**8-Puzzle Solver** là một dự án sử dụng Python để triển khai nhiều thuật toán AI nhằm giải bài toán 8-Puzzle – một bài toán kinh điển về sắp xếp ô số. Dự án bao gồm các nhóm thuật toán như tìm kiếm không thông tin, tìm kiếm có thông tin, tìm kiếm cục bộ, tìm kiếm trong môi trường phức tạp, tìm kiếm có điều kiện ràng buộc, và học tăng cường. Ngoài ra, dự án cung cấp một giao diện GUI bằng Tkinter để người dùng có thể theo dõi trực quan quá trình giải, là công cụ tuyệt vời để học tập và so sánh các kỹ thuật AI.

---

## 📑 Mục lục

1. [Tổng quan dự án](#-tổng-quan-dự-án)
2. [Mục tiêu](#-mục-tiêu)
3. [Nội dung dự án](#-nội-dung-dự-án)
4. [Thuật toán](#-thuật-toán)
   - [Tìm kiếm không thông tin (Uninformed Search)](#tìm-kiếm-không-thông-tin-uninformed-search)
     - [Breadth-First Search (BFS)](#breadth-first-search-bfs)
     - [Depth-First Search (DFS)](#depth-first-search-dfs)
     - [Uniform Cost Search (UCS)](#uniform-cost-search-ucs)
     - [Iterative Deepening Search (IDS)](#iterative-deepening-search-ids)
     - [So sánh các thuật toán Uninformed Search](#so-sánh-các-thuật-toán-uninformed-search)
   - [Tìm kiếm có thông tin (Informed Search)](#tìm-kiếm-có-thông-tin-informed-search)
     - [Greedy Best-First Search](#greedy-best-first-search)
     - [A* Search](#a-search)
     - [Iterative Deepening A* (IDA*)](#iterative-deepening-a-ida)
   - [Tìm kiếm cục bộ (Local Search)](#tìm-kiếm-cục-bộ-local-search)
     - [Best Hill Climbing](#best-hill-climbing)
     - [Simulated Annealing](#simulated-annealing)
     - [Beam Search](#beam-search)
   - [Tìm kiếm trong môi trường phức tạp (Complex Environment Search)](#tìm-kiếm-trong-môi-trường-phức-tạp-complex-environment-search)
     - [Partially Observable Search](#partially-observable-search)
     - [No Observation Search](#no-observation-search)
     - [AND-OR Search Algorithm](#and-or-search-algorithm)
   - [Tìm kiếm có điều kiện ràng buộc (Constraint Satisfaction Problem)](#tìm-kiếm-có-điều-kiện-ràng-buộc-constraint-satisfaction-problem)
     - [Constraint Testing](#constraint-testing)
     - [Backtracking CSP](#backtracking-csp)
     - [Backtracking AC-3](#backtracking-ac-3)
   - [Học tăng cường (Reinforcement Learning)](#học-tăng-cường-reinforcement-learning)
     - [Q-Learning](#q-learning)
5. [Cài đặt](#-cài-đặt)
6. [Hướng dẫn sử dụng](#-hướng-dẫn-sử-dụng)
7. [Cấu trúc thư mục](#-cấu-trúc-thư-mục)
8. [Minh họa](#-minh-họa)
9. [Kết luận](#-kết-luận)
10. [Tác giả](#-tác-giả)
11. [Đóng góp](#-đóng-góp)
12. [Giấy phép](#-giấy-phép)
13. [Liên hệ](#-liên-hệ)

---

## 🎯 Mục tiêu

- **Triển khai các thuật toán AI**: Ứng dụng nhiều thuật toán tìm kiếm (uninformed, informed, local search, complex environment, constraint satisfaction, reinforcement learning) để giải bài toán 8-puzzle, giúp người dùng hiểu rõ cách hoạt động và hiệu suất của từng thuật toán.
- **So sánh hiệu suất**: Phân tích và so sánh hiệu quả của các thuật toán về thời gian chạy, bộ nhớ sử dụng, và tính tối ưu của đường đi để hiểu rõ ưu/nhược điểm của từng thuật toán.
- **Trực quan hóa**: Cung cấp giao diện đồ họa (GUI) để người dùng có thể theo dõi quá trình giải bài toán một cách trực quan.

---

## 📝 Nội dung dự án

Dự án **8-Puzzle Visualizer** triển khai bài toán 8-puzzle, một bài toán cổ điển trong Trí tuệ Nhân tạo, với mục tiêu sắp xếp các ô số từ trạng thái ban đầu về trạng thái mục tiêu thông qua việc di chuyển ô trống. Dự án tích hợp **bảy nhóm thuật toán** tìm kiếm, bao gồm:

- **Tìm kiếm không thông tin (Uninformed Search)**: Các thuật toán dựa trên khám phá mù, không sử dụng hàm heuristic.
- **Tìm kiếm có thông tin (Informed Search)**: Các thuật toán sử dụng heuristic để hướng dẫn tìm kiếm một cách hiệu quả hơn.
- **Tìm kiếm cục bộ (Local Search)**: Các thuật toán cải thiện trạng thái dần dần dựa trên hàm đánh giá.
- **Tìm kiếm trong môi trường phức tạp (Complex Environment Search)**: Các thuật toán xử lý các tình huống không xác định hoặc quan sát không đầy đủ.
- **Tìm kiếm có điều kiện ràng buộc (Constraint Satisfaction Problem)**: Các thuật toán giải bài toán bằng cách gán các giá trị thỏa mãn các ràng buộc.
- **Học tăng cường (Reinforcement Learning)**: Các thuật toán học từ kinh nghiệm để tìm lời giải tối ưu.
- **Tìm kiếm không xác định (Non-deterministic Search)**: Các thuật toán xử lý các tình huống không xác định hoặc có nhiều điều kiện phức tạp.

Mỗi nhóm được trình bày chi tiết với:
- **Thành phần chính của bài toán**: Mô tả trạng thái, hành động, kiểm tra mục tiêu, và hàm heuristic (nếu có).
- **Lời giải**: Chuỗi trạng thái và hành động từ trạng thái ban đầu đến mục tiêu.
- **GIF minh họa**: Hình ảnh động thể hiện quá trình giải của từng thuật toán.
- **So sánh hiệu suất**: Bảng so sánh ghi lại thời gian thực thi và số lần mở rộng (expansions) để so sánh (cùng trạng thái ban đầu và mục tiêu).
- **Nhận xét**: Phân tích ưu điểm, nhược điểm và hiệu quả khi áp dụng vào bài toán 8-puzzle.

---

## 🛠️ Thuật toán

Dự án triển khai một loạt thuật toán AI đa dạng, được phân loại thành bảy nhóm chính:

### Tìm kiếm không thông tin (Uninformed Search)

#### Breadth-First Search (BFS)
- **Mô tả**: BFS (Tìm kiếm theo chiều rộng) khám phá tất cả các trạng thái theo từng cấp độ độ sâu, từ trạng thái ban đầu đến trạng thái mục tiêu, sử dụng hàng đợi (queue).
- **Phân tích lý thuyết**:
  - **Tính tối ưu**: Đảm bảo tìm ra con đường ngắn nhất trong không gian tìm kiếm không có trọng số.
  - **Hoạt động**: Mở rộng tất cả trạng thái ở độ sâu hiện tại trước khi đi sâu hơn.
  - **Quản lý vòng lặp**: Sử dụng tập hợp `visited` để tránh lặp lại trạng thái.
- **Ưu điểm**:
  - Đảm bảo tính tối ưu và hoàn chỉnh.
- **Nhược điểm**:
  - Tiêu tốn nhiều bộ nhớ.
  - Thời gian chạy chậm nếu độ sâu lớn.
- **Độ phức tạp**:
  - **Thời gian**: \( O(b^d) \), với \( b \) là nhánh trung bình (2-4), \( d \) là độ sâu mục tiêu.
  - **Bộ nhớ**: \( O(b^d) \).
- **Hình ảnh minh họa**: ![GIF mô tả BFS](assets/gif_solve/BFS.gif)
- **Hình ảnh bổ sung**: ![BFS](https://upload.wikimedia.org/wikipedia/commons/f/f5/BFS-Algorithm_Search_Way.gif)
- **Liên kết**: [Wikipedia - Breadth-first search](https://en.wikipedia.org/wiki/Breadth-first-search)
- **Nhận xét**: BFS lý tưởng khi cần giải pháp tối ưu, nhưng tốn bộ nhớ và chậm với độ sâu lớn.

#### Depth-First Search (DFS)
- **Mô tả**: DFS (Tìm kiếm theo chiều sâu) khám phá sâu nhất một nhánh trước khi quay lui, sử dụng ngăn xếp (stack) hoặc đệ quy.
- **Phân tích lý thuyết**:
  - **Tính tối ưu**: Không đảm bảo đường đi ngắn nhất.
  - **Hoạt động**: Đi sâu vào một nhánh, quay lui nếu không tìm thấy mục tiêu.
  - **Quản lý vòng lặp**: Sử dụng tập hợp `visited` để tránh lặp.
- **Ưu điểm**:
  - Tiết kiệm bộ nhớ.
  - Nhanh nếu nhánh đầu chứa mục tiêu.
- **Nhược điểm**:
  - Không tối ưu, có nguy cơ tràn ngăn xếp.
- **Độ phức tạp**:
  - **Thời gian**: \( O(b^d) \).
  - **Bộ nhớ**: \( O(d) \).
- **Hình ảnh minh họa**: ![GIF mô tả DFS](assets/gif_solve/DFS.gif)
- **Hình ảnh bổ sung**: ![DFS](https://upload.wikimedia.org/wikipedia/commons/7/7f/Depth-First-Search.gif)
- **Liên kết**: [Wikipedia - Depth-first search](https://en.wikipedia.org/wiki/Depth-first-search)
- **Nhận xét**: DFS phù hợp khi bộ nhớ hạn chế, nhưng không hiệu quả nếu cần đường đi tối ưu.

#### Uniform Cost Search (UCS)
- **Mô tả**: UCS mở rộng trạng thái dựa trên chi phí thấp nhất từ trạng thái ban đầu, sử dụng hàng đợi ưu tiên.
- **Phân tích lý thuyết**:
  - **Tính tối ưu**: Đảm bảo đường đi ngắn nhất trong không gian có trọng số.
  - **Hoạt động**: Chọn trạng thái có chi phí thấp nhất để mở rộng.
  - **Quản lý vòng lặp**: Sử dụng tập hợp `visited` và cập nhật nếu tìm thấy chi phí thấp hơn.
- **Ưu điểm**:
  - Đảm bảo tính tối ưu và hoàn chỉnh.
- **Nhược điểm**:
  - Tiêu tốn nhiều bộ nhớ, tương tự BFS.
- **Độ phức tạp**:
  - **Thời gian**: \( O(b^{C*/ε}) \), với \( C* \) là chi phí tối ưu, \( ε = 1 \).
  - **Bộ nhớ**: \( O(b^{C*/ε}) \).
- **Hình ảnh minh họa**: ![GIF mô tả UCS](assets/gif_solve/UCS.gif)
- **Hình ảnh bổ sung**: ![UCS](https://cs.stanford.edu/people/eroberts/courses/soco/projects/2003-04/intelligent-search/dijkstra.gif)
- **Liên kết**: [GeeksforGeeks - Uniform Cost Search](https://www.geeksforgeeks.org/uniform-cost-search-ucs-in-ai/)
- **Nhận xét**: UCS hiệu quả khi cần giải pháp tối ưu, nhưng không vượt trội so với BFS trong 8-puzzle do chi phí đồng nhất.

#### Iterative Deepening Search (IDS)
- **Mô tả**: IDS kết hợp BFS và DFS, thực hiện DFS với giới hạn độ sâu tăng dần.
- **Phân tích lý thuyết**:
  - **Tính tối ưu**: Đảm bảo đường đi ngắn nhất trong không gian không có trọng số.
  - **Hoạt động**: Lặp DFS với độ sâu tăng dần cho đến khi tìm thấy mục tiêu.
  - **Quản lý vòng lặp**: Sử dụng tập hợp `visited` trong mỗi lần lặp.
- **Ưu điểm**:
  - Tối ưu và tiết kiệm bộ nhớ hơn BFS.
- **Nhược điểm**:
  - Chậm hơn BFS do lặp lại nhiều lần.
- **Độ phức tạp**:
  - **Thời gian**: \( O(b^d) \), chậm hơn BFS do lặp.
  - **Bộ nhớ**: \( O(bd) \).
- **Hình ảnh minh họa**: ![GIF mô tả IDS](assets/gif_solve/IDS.gif)
- **Liên kết**: [GeeksforGeeks - Iterative Deepening Search](https://www.geeksforgeeks.org/iterative-deepening-searchids-iterative-deepening-depth-first-searchiddfs/)
- **Nhận xét**: IDS cân bằng giữa tính tối ưu và bộ nhớ, nhưng chậm hơn BFS.

#### So sánh các thuật toán Uninformed Search
- **Hình ảnh so sánh hiệu suất**: ![So sánh hiệu suất Uninformed Search](assets/UninformedSearchCMP.jpg)
- **Nhận xét**: BFS và UCS đảm bảo tính tối ưu nhưng tốn bộ nhớ; DFS tiết kiệm bộ nhớ nhưng không tối ưu; IDS cân bằng nhưng chậm hơn.

### Tìm kiếm có thông tin (Informed Search)

#### Greedy Best-First Search
- **Mô tả**: Chọn trạng thái có giá trị heuristic thấp nhất để mở rộng, sử dụng hàng đợi ưu tiên.
- **Phân tích lý thuyết**:
  - **Tính tối ưu**: Không đảm bảo đường đi ngắn nhất.
  - **Hàm heuristic**: Khoảng cách Manhattan.
  - **Hoạt động**: Ưu tiên trạng thái có heuristic thấp nhất.
  - **Quản lý vòng lặp**: Sử dụng tập hợp `visited`.
- **Ưu điểm**:
  - Nhanh hơn uninformed search.
  - Tiết kiệm bộ nhớ nếu heuristic tốt.
- **Nhược điểm**:
  - Không tối ưu, phụ thuộc vào heuristic.
- **Độ phức tạp**:
  - **Thời gian**: \( O(b^d) \).
  - **Bộ nhớ**: \( O(b^d) \).
- **Hình ảnh minh họa**: ![GIF mô tả GBFS](assets/gif_solve/GBFS.gif)
- **Hình ảnh bổ sung**: ![Greedy Best-First Search](https://media.geeksforgeeks.org/wp-content/uploads/20240919162457/Greedy-best-First-Search-in-AI.png)
- **Liên kết**: [GeeksforGeeks - Greedy Best-First Search](https://www.geeksforgeeks.org/greedy-best-first-search-algorithm/)
- **Nhận xét**: GBFS nhanh hơn uninformed search nhưng không tối ưu, hiệu quả phụ thuộc vào heuristic.

#### A* Search
- **Mô tả**: Kết hợp chi phí đã đi \( g \) và heuristic \( h \), chọn trạng thái có \( f = g + h \) thấp nhất.
- **Phân tích lý thuyết**:
  - **Tính tối ưu**: Đảm bảo đường đi ngắn nhất nếu heuristic admissible và consistent.
  - **Hàm heuristic**: Khoảng cách Manhattan.
  - **Hoạt động**: Mở rộng trạng thái có \( f \) thấp nhất.
  - **Quản lý vòng lặp**: Cập nhật đường đi nếu tìm thấy \( f \) thấp hơn.
- **Ưu điểm**:
  - Tối ưu và hiệu quả hơn BFS.
- **Nhược điểm**:
  - Tốn bộ nhớ.
- **Độ phức tạp**:
  - **Thời gian**: \( O(b^d) \), nhanh hơn BFS.
  - **Bộ nhớ**: \( O(b^d) \).
- **Hình ảnh minh họa**: ![GIF mô tả A*](assets/gif_solve/AStar.gif)
- **Hình ảnh bổ sung**: ![A* Search](https://upload.wikimedia.org/wikipedia/commons/5/5d/Astar_progress_animation.gif)
- **Liên kết**: [GeeksforGeeks - A* Search Algorithm](https://www.geeksforgeeks.org/a-search-algorithm/)
- **Nhận xét**: A* là thuật toán hiệu quả nhất trong nhóm informed search cho 8-puzzle, nhưng tốn bộ nhớ.

#### Iterative Deepening A* (IDA*)
- **Mô tả**: Kết hợp IDS và A*, sử dụng ngưỡng \( f = g + h \) tăng dần.
- **Phân tích lý thuyết**:
  - **Tính tối ưu**: Đảm bảo nếu heuristic admissible và consistent.
  - **Hoạt động**: Thực hiện DFS với ngưỡng \( f \), tăng ngưỡng nếu không tìm thấy mục tiêu.
- **Ưu điểm**:
  - Tối ưu, tiết kiệm bộ nhớ hơn A*.
- **Nhược điểm**:
  - Chậm hơn A* do lặp lại.
- **Độ phức tạp**:
  - **Thời gian**: \( O(b^d) \).
  - **Bộ nhớ**: \( O(d) \).
- **Hình ảnh minh họa**: ![GIF mô tả IDA*](assets/gif_solve/IDAStar.gif)
- **Liên kết**: [GeeksforGeeks - Iterative Deepening A*](https://www.geeksforgeeks.org/iterative-deepening-a-algorithm-ida-artificial-intelligence/)
- **Nhận xét**: IDA* phù hợp khi cần tiết kiệm bộ nhớ, nhưng chậm hơn A*.

### Tìm kiếm cục bộ (Local Search)

#### Best Hill Climbing
- **Mô tả**: Chọn trạng thái con có heuristic tốt hơn trạng thái hiện tại.
- **Phân tích lý thuyết**:
  - **Tính tối ưu**: Không đảm bảo, dễ mắc kẹt tại cực trị cục bộ.
  - **Hoạt động**: Di chuyển theo hướng tăng heuristic.
- **Ưu điểm**:
  - Nhanh, tiết kiệm bộ nhớ.
- **Nhược điểm**:
  - Dễ mắc kẹt, không tối ưu.
- **Độ phức tạp**:
  - **Thời gian**: Phụ thuộc vào số lần lặp.
  - **Bộ nhớ**: \( O(1) \).
- **Hình ảnh minh họa**: ![GIF mô tả Hill Climbing](assets/gif_solve/HillClimbing.gif)
- **Liên kết**: [GeeksforGeeks - Hill Climbing](https://www.geeksforgeeks.org/introduction-hill-climbing-artificial-intelligence/)
- **Nhận xét**: Best Hill Climbing nhanh nhưng dễ bị kẹt tại cực trị cục bộ, không đảm bảo giải pháp tối ưu.

#### Simulated Annealing
- **Mô tả**: Chấp nhận trạng thái con tệ hơn với xác suất giảm dần, mô phỏng làm nguội kim loại.
- **Phân tích lý thuyết**:
  - **Tính tối ưu**: Có thể tối ưu nếu lịch làm nguội chậm.
  - **Hoạt động**: Chọn trạng thái con ngẫu nhiên, chấp nhận dựa trên nhiệt độ.
- **Ưu điểm**:
  - Thoát cực trị cục bộ, linh hoạt.
- **Nhược điểm**:
  - Phụ thuộc vào lịch làm nguội.
- **Độ phức tạp**:
  - **Thời gian**: Phụ thuộc vào số lần lặp.
  - **Bộ nhớ**: \( O(1) \).
- **Hình ảnh minh họa**: ![GIF mô tả Simulated Annealing](assets/gif_solve/SimulatedAnnealing.gif)
- **Liên kết**: [Wikipedia - Simulated Annealing](https://en.wikipedia.org/wiki/Simulated_annealing)
- **Nhận xét**: Simulated Annealing linh hoạt hơn Hill Climbing, nhưng hiệu quả phụ thuộc vào tham số.

#### Beam Search
- **Mô tả**: Giới hạn số trạng thái giữ lại tại mỗi bước (beam width), chọn \( k \) trạng thái tốt nhất dựa trên heuristic.
- **Phân tích lý thuyết**:
  - **Tính tối ưu**: Không đảm bảo, có thể bỏ qua đường đi tốt nhất.
  - **Hoạt động**: Mở rộng \( k \) trạng thái tốt nhất, giữ lại \( k \) trạng thái con tốt nhất.
  - **Quản lý vòng lặp**: Giới hạn số trạng thái để tránh lặp vô hạn.
- **Ưu điểm**:
  - Tiết kiệm bộ nhớ, nhanh nếu \( k \) nhỏ.
  - Linh hoạt điều chỉnh \( k \).
- **Nhược điểm**:
  - Không tối ưu, phụ thuộc vào \( k \) và heuristic.
- **Độ phức tạp**:
  - **Thời gian**: \( O(kbd) \), với \( b \) là nhánh, \( d \) là độ sâu.
  - **Bộ nhớ**: \( O(k) \).
- **Hình ảnh minh họa**: ![GIF mô tả Beam Search](assets/gif_solve/BeamSearch.gif)
- **Hình ảnh bổ sung**: ![Beam Search](https://upload.wikimedia.org/wikipedia/commons/2/23/Beam_search.gif)
- **Liên kết**: [GeeksforGeeks - Beam Search](https://www.geeksforgeeks.org/introduction-to-beam-search-algorithm/)
- **Nhận xét**: Beam Search phù hợp khi cần cân bằng giữa tốc độ và chất lượng, nhưng không đảm bảo giải pháp tối ưu trong 8-puzzle.

### Tìm kiếm trong môi trường phức tạp (Complex Environment Search)

#### Partially Observable Search
- **Mô tả**: Xử lý bài toán 8-puzzle trong môi trường chỉ quan sát được một phần (ví dụ: không biết trạng thái đầy đủ của bảng).
- **Phân tích lý thuyết**:
  - **Tính tối ưu**: Không đảm bảo do thiếu thông tin.
  - **Hoạt động**: Sử dụng mô hình niềm tin (belief state) để ước lượng trạng thái thực tế, chọn hành động dựa trên xác suất.
  - **Quản lý vòng lặp**: Cập nhật niềm tin sau mỗi hành động và quan sát.
- **Ưu điểm**:
  - Phù hợp với môi trường không xác định.
  - Có thể mô phỏng các tình huống thực tế hơn.
- **Nhược điểm**:
  - Phức tạp, tốn tài nguyên để duy trì niềm tin.
  - Không hiệu quả trong 8-puzzle do bài toán thường xác định.
- **Độ phức tạp**:
  - **Thời gian**: \( O(b^d \cdot |B|) \), với \( B \) là không gian niềm tin.
  - **Bộ nhớ**: \( O(|B|) \).
- **Hình ảnh minh họa**: ![GIF mô tả Partially Observable Search](assets/gif_solve/PartiallyObservableSearch.gif)
- **Liên kết**: [Wikipedia - Partially Observable Markov Decision Process](https://en.wikipedia.org/wiki/Partially_observable_Markov_decision_process)
- **Nhận xét**: Partially Observable Search phù hợp cho các bài toán thực tế hơn, nhưng không cần thiết trong 8-puzzle do môi trường xác định.

#### No Observation Search
- **Mô tả**: Xử lý bài toán 8-puzzle mà không có quan sát trực tiếp, dựa trên chiến lược cố định hoặc hành động ngẫu nhiên.
- **Phân tích lý thuyết**:
  - **Tính tối ưu**: Không đảm bảo, gần như không khả thi.
  - **Hoạt động**: Thực hiện chuỗi hành động cố định hoặc ngẫu nhiên, kiểm tra trạng thái mục tiêu khi có thể.
  - **Quản lý vòng lặp**: Giới hạn số bước để tránh lặp vô hạn.
- **Ưu điểm**:
  - Đơn giản, không cần quản lý trạng thái phức tạp.
- **Nhược điểm**:
  - Hầu như không hiệu quả trong 8-puzzle do thiếu thông tin.
  - Phụ thuộc vào may mắn.
- **Độ phức tạp**:
  - **Thời gian**: \( O(b^d) \), nhưng thường không tìm được giải pháp.
  - **Bộ nhớ**: \( O(1) \).
- **Hình ảnh minh họa**: ![GIF mô tả No Observation Search](assets/gif_solve/NoObservationSearch.gif)
- **Liên kết**: [Wikipedia - Open-Loop Controller](https://en.wikipedia.org/wiki/Open-loop_controller)
- **Nhận xét**: No Observation Search không thực tế cho 8-puzzle, chỉ mang tính lý thuyết.

#### AND-OR Search Algorithm
- **Mô tả**: Xử lý bài toán với nhánh AND/OR, xây dựng cây tìm kiếm thỏa mãn điều kiện phức tạp.
- **Phân tích lý thuyết**:
  - **Tính tối ưu**: Phụ thuộc vào triển khai, không luôn tối ưu.
  - **Hoạt động**: Xây dựng cây với nút AND (tất cả điều kiện con đúng) và OR (một điều kiện con đúng).
  - **Quản lý vòng lặp**: Kiểm tra trạng thái để tránh lặp.
- **Ưu điểm**:
  - Phù hợp với bài toán không xác định.
- **Nhược điểm**:
  - Phức tạp, tốn tài nguyên nếu không gian lớn.
- **Độ phức tạp**:
  - **Thời gian**: \( O(b^d) \).
  - **Bộ nhớ**: \( O(b^d) \).
- **Hình ảnh minh họa**: ![GIF mô tả AND-OR Search](assets/gif_solve/ANDORSearch.gif)
- **Liên kết**: [Wikipedia - AND-OR Search](https://en.wikipedia.org/wiki/AND%E2%80%93OR_search_algorithm)
- **Nhận xét**: AND-OR Search phù hợp cho các bài toán phức tạp, nhưng ít hiệu quả trong 8-puzzle do tính chất xác định của bài toán.

### Tìm kiếm có điều kiện ràng buộc (Constraint Satisfaction Problem)

#### Constraint Testing
- **Mô tả**: Kiểm tra các trạng thái của 8-puzzle để đảm bảo thỏa mãn các ràng buộc, như mỗi ô chỉ chứa một số duy nhất và ô trống có thể di chuyển hợp lệ.
- **Phân tích lý thuyết**:
  - **Tính tối ưu**: Đảm bảo trạng thái hợp lệ, nhưng không đảm bảo đường đi tối ưu.
  - **Hoạt động**: Kiểm tra từng trạng thái con để đảm bảo các số từ 0-8 xuất hiện đúng một lần và các di chuyển (lên, xuống, trái, phải) hợp lệ.
  - **Quản lý vòng lặp**: Sử dụng tập hợp trạng thái đã kiểm tra để tránh lặp.
- **Ưu điểm**:
  - Đơn giản, dễ triển khai để kiểm tra tính hợp lệ.
  - Hỗ trợ các thuật toán khác bằng cách loại bỏ trạng thái không hợp lệ.
- **Nhược điểm**:
  - Không trực tiếp tìm lời giải, chỉ hỗ trợ kiểm tra.
  - Có thể tốn thời gian nếu số trạng thái lớn.
- **Độ phức tạp**:
  - **Thời gian**: \( O(1) \) cho mỗi kiểm tra trạng thái, nhưng tổng thời gian phụ thuộc vào số trạng thái.
  - **Bộ nhớ**: \( O(1) \) cho mỗi kiểm tra.
- **Hình ảnh minh họa**: ![GIF mô tả Constraint Testing](assets/gif_solve/ConstraintTesting.gif)
- **Liên kết**: [GeeksforGeeks - Constraint Satisfaction Problems](https://www.geeksforgeeks.org/constraint-satisfaction-problems-csp-in-artificial-intelligence/)
- **Nhận xét**: Constraint Testing hữu ích để đảm bảo tính hợp lệ của trạng thái trong 8-puzzle, nhưng cần kết hợp với các thuật toán tìm kiếm khác để tìm lời giải.

#### Backtracking CSP
- **Mô tả**: Sử dụng tìm kiếm quay lui để gán giá trị cho các ô trong 8-puzzle, đảm bảo thỏa mãn các ràng buộc (mỗi số xuất hiện một lần, di chuyển hợp lệ).
- **Phân tích lý thuyết**:
  - **Tính tối ưu**: Không đảm bảo đường đi ngắn nhất, nhưng đảm bảo trạng thái hợp lệ.
  - **Hoạt động**: Gán giá trị cho từng ô, quay lui nếu vi phạm ràng buộc, tiếp tục cho đến khi đạt trạng thái mục tiêu.
  - **Quản lý vòng lặp**: Quay lui tự động tránh lặp trạng thái không hợp lệ.
- **Ưu điểm**:
  - Hiệu quả trong việc tìm trạng thái hợp lệ.
  - Có thể kết hợp với heuristic để cải thiện tốc độ.
- **Nhược điểm**:
  - Chậm nếu không gian trạng thái lớn.
  - Không tối ưu về số bước di chuyển.
- **Độ phức tạp**:
  - **Thời gian**: \( O(b^d) \), với \( b \) là số giá trị có thể gán, \( d \) là số ô.
  - **Bộ nhớ**: \( O(d) \) cho ngăn xếp quay lui.
- **Hình ảnh minh họa**: ![GIF mô tả Backtracking CSP](assets/gif_solve/BacktrackingCSP.gif)
- **Liên kết**: [GeeksforGeeks - Backtracking CSP](https://www.geeksforgeeks.org/constraint-satisfaction-problems-csp-in-artificial-intelligence/)
- **Nhận xét**: Backtracking CSP phù hợp để kiểm tra tính khả thi, nhưng không hiệu quả trong việc tìm đường đi tối ưu cho 8-puzzle.

#### Backtracking AC-3
- **Mô tả**: Kết hợp Backtracking CSP với thuật toán AC-3 để duy trì tính nhất quán cung (arc consistency), giảm không gian tìm kiếm bằng cách loại bỏ các giá trị không hợp lệ trước khi quay lui.
- **Phân tích lý thuyết**:
  - **Tính tối ưu**: Không đảm bảo đường đi ngắn nhất.
  - **Hoạt động**: Sử dụng AC-3 để loại bỏ các giá trị không thỏa mãn ràng buộc, sau đó áp dụng quay lui để gán giá trị.
  - **Quản lý vòng lặp**: AC-3 giảm số trạng thái cần kiểm tra.
- **Ưu điểm**:
  - Hiệu quả hơn Backtracking CSP nhờ giảm không gian tìm kiếm.
  - Đảm bảo tính hợp lệ của trạng thái.
- **Nhược điểm**:
  - Phức tạp hơn Backtracking CSP.
  - Vẫn không tối ưu về số bước.
- **Độ phức tạp**:
  - **Thời gian**: \( O(b^d) \), nhưng nhanh hơn Backtracking CSP nhờ AC-3.
  - **Bộ nhớ**: \( O(d) \).
- **Hình ảnh minh họa**: ![GIF mô tả Backtracking AC-3](assets/gif_solve/BacktrackingAC3.gif)
- **Liên kết**: [Wikipedia - AC-3 Algorithm](https://en.wikipedia.org/wiki/AC-3_algorithm)
- **Nhận xét**: Backtracking AC-3 cải thiện hiệu suất so với Backtracking CSP, nhưng vẫn không lý tưởng cho 8-puzzle do không tối ưu đường đi.

### Học tăng cường (Reinforcement Learning)

#### Q-Learning
- **Mô tả**: Q-Learning là một thuật toán học tăng cường, học cách chọn hành động tối ưu thông qua thử-và-sai, dựa trên bảng Q lưu trữ giá trị hành động-trạng thái.
- **Phân tích lý thuyết**:
  - **Tính tối ưu**: Có thể đạt giải pháp tối ưu nếu học đủ lâu và tham số được điều chỉnh tốt.
  - **Hoạt động**: Cập nhật bảng Q dựa trên phần thưởng (ví dụ: -1 cho mỗi bước, +100 khi đạt mục tiêu). Chọn hành động dựa trên giá trị Q cao nhất hoặc ngẫu nhiên (epsilon-greedy).
  - **Quản lý vòng lặp**: Tránh lặp vô hạn bằng cách giới hạn số bước hoặc sử dụng epsilon decay.
- **Ưu điểm**:
  - Học từ kinh nghiệm, không cần mô hình môi trường.
  - Có thể thích nghi với các trạng thái mới.
- **Nhược điểm**:
  - Chậm để hội tụ trong không gian trạng thái lớn (8-puzzle có \( 9!/2 = 181,440 \) trạng thái khả thi).
  - Phụ thuộc vào tham số (alpha, gamma, epsilon).
- **Độ phức tạp**:
  - **Thời gian**: Phụ thuộc vào số lần lặp và kích thước không gian trạng thái.
  - **Bộ nhớ**: \( O(|S| \cdot |A|) \), với \( S \) là số trạng thái, \( A \) là số hành động.
- **Hình ảnh minh họa**: ![GIF mô tả Q-Learning](assets/gif_solve/QLearning.gif)
- **Liên kết**: [GeeksforGeeks - Q-Learning](https://www.geeksforgeeks.org/q-learning-in-python/)
- **Nhận xét**: Q-Learning phù hợp cho các bài toán cần học dài hạn, nhưng không hiệu quả trong 8-puzzle do không gian trạng thái lớn và yêu cầu tính tối ưu nhanh.

---

## 🖥️ Cài đặt

Để chạy dự án trên máy của bạn, hãy làm theo các bước sau:

1. **Clone repository**:
   ```bash
   git clone https://github.com/taidang05/8_Puzzles_AI_Project.git
   cd 8_Puzzles_AI_Project
