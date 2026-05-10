public class BinarySearchDemo {

    public static void searchNumber(Integer key) {

        List<Integer> nums = new List<Integer>{1,2,3,4,5,6,7,8};

        Integer start = 0;
        Integer endPos = nums.size() - 1;

        Boolean found = false;

        while(start <= endPos) {

            Integer mid = (start + endPos) / 2;

            if(nums[mid] == key) {

                found = true;
                break;

            } else if(key < nums[mid]) {

                endPos = mid - 1;

            } else {

                start = mid + 1;
            }
        }

        if(found) {
            System.debug('Element Found');
        } else {
            System.debug('Element Not Found');
        }
    }
}
