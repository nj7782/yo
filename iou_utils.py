def calculate_iou(x1, y1, w1, h1, x2, y2, w2, h2):
    """Calculates the Intersection over Union (IoU) between two bounding boxes.

    Args:
        x1, y1, w1, h1: Coordinates and dimensions of the first bounding box.
        x2, y2, w2, h2: Coordinates and dimensions of the second bounding box.

    Returns:
        The IoU value between the two bounding boxes.
    """

    # Calculate the coordinates of the intersection rectangle
    x_overlap = max(0, min(x1 + w1, x2 + w2) - max(x1, x2))
    y_overlap = max(0, min(y1 + h1, y2 + h2) - max(y1, y2))
    intersection_area = x_overlap * y_overlap

    # Calculate the union area
    union_area = w1 * h1 + w2 * h2 - intersection_area

    # Calculate the IoU
    iou = intersection_area / union_area
    return iou
