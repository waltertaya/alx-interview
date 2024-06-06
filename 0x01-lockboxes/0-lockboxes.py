#!/usr/bin/python3
"""Solves the lock boxes puzzle"""


def find_next_open_box(open_boxes):
    """Finds the next box that has been opened but not yet checked.

    Args:
        open_boxes (dict): Dictionary containing the status of opened boxes.

    Returns:
        list: List of keys contained in the next box to check.
    """
    for index, box in open_boxes.items():
        if box.get('status') == 'opened':
            box['status'] = 'opened/checked'
            return box.get('keys')
    return None


def canUnlockAll(boxes):
    """Determines if all boxes can be opened.

    Args:
        boxes (list): List of lists, where each inner
        list contains keys for other boxes.

    Returns:
        bool: True if all boxes can be opened, otherwise False.
    """
    if len(boxes) <= 1 or boxes == [[]]:
        return True

    opened_boxes = {}
    while True:
        if len(opened_boxes) == 0:
            opened_boxes[0] = {
                'status': 'opened',
                'keys': boxes[0],
            }
        keys = find_next_open_box(opened_boxes)
        if keys:
            for key in keys:
                try:
                    opened_boxe = opened_boxes.get(key)
                    opened_boxed = opened_boxes.get(key).get('status')
                    if opened_boxe and opened_boxed == 'opened/checked':
                        continue
                    opened_boxes[key] = {
                        'status': 'opened',
                        'keys': boxes[key]
                    }
                except (KeyError, IndexError):
                    continue
        elif 'opened' in [box.get('status') for box in opened_boxes.values()]:
            continue
        elif len(opened_boxes) == len(boxes):
            break
        else:
            return False

    return len(opened_boxes) == len(boxes)


def main():
    """Entry point"""
    print(canUnlockAll([[]]))


if __name__ == '__main__':
    main()
