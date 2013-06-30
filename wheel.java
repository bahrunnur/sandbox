public class Wheel {

    private int capacity;
    private int[] datas;
    private int end;

    Wheel(int capacity) {
        this.capacity = capacity;
        this.datas = new int[capacity];
        this.end = 0;
    }

    public void addData(int data) {
        if (isFull()) {
            System.out.println("Wheel is full");
        } else {
            this.datas[this.end] = data;
            this.end += 1;            
        }
    }

    public int getData() {
        int middle = (this.capacity - 1) / 2;
        return this.datas[middle];
    }

    public boolean isFull() {
        return (this.end == this.capacity - 1);
    }

    public boolean isEmpty() {
        return (this.end == 0);
    }

    public void rotateClockWise() {
        this.capacity -= 2;
    }

    public void rotateCounterClockWise() {
        this.capacity += 2;
    }

}

public static void main(String[] args) {
    Wheel roda = new Wheel(10);
    roda.addData(5);
    roda.addData(12);
    roda.addData(70);
    roda.addData(54);
    int x = roda.getData(); // return null karena data yang ditengah wheel masih kosong
    roda.addData(72);
    int a = roda.getData(); // return 72
    roda.rotateClockWise();
    int y = roda.getData(); // return 54
    roda.rotateClockWise();
    int b = roda.getData(); // return 70
}