from glob import glob

splitter = '------------------------------------------------------------------------------------------------------------------------------------'

tegr = ['## 参考（Reference）', '## 解释（Explanations）']


def get_category_correctness_count(file_path):
    num_correct = 0
    num_total = 0
    why_wrong = set()

    with (open(file_path, 'r') as f):
        # TODO Since we're not trying to extract categorized content, maybe a simple regex match for
        #  each line will just work
        blocks = f.read().split(splitter)
        for block in blocks:
            block_content = block.strip()
            block_parts = block_content.split('\n')
            first_line = block_parts[0]

            test_line = first_line
            if first_line in tegr and len(block_parts) > 1:
                second_line = block_parts[1]
                test_line = second_line

            if '正确' in test_line or '错误' in test_line:
                num_total += 1
                if '正确' in test_line:
                    num_correct += 1
                else:
                    # Collect why it's wrong
                    why_wrong.add(test_line.split()[-1])
                # Print it for debugging
                # print(test_line)
    return num_total, num_correct, why_wrong


overall_total = 0
overall_correct = 0

for file_path in glob('./**/refactor/*.md'):
# for file_path in glob('./kubernetes/refactor/deploying-control-plane-components.md'):
    num_total, num_correct, why_wrong = get_category_correctness_count(file_path)
    print(file_path, num_total, num_correct, ','.join(list(why_wrong)))

    overall_total += num_total
    overall_correct += num_correct

print('\n\nnum blocks:', overall_total, ', num correctly categorized blocks:', overall_correct)
