#define fake_size 0x41

int main(void)
{
    void *ptr;

    ptr=malloc(0x10);
    ptr=(void *)((int)ptr+24);

    *((long long*)ptr)=fake_size; // overwrite top chunk size

    malloc(0x60);

    malloc(0x60);
}
