
program multiples
    s = 0
    do i=1,999
        if ((mod(i,3)==0) .OR. (mod(i,5)==0)) then
            s = s+i
        end if
    end do
    print*, s
end program multiples

---

(setq s 0)
(loop for i from 1 to 999
      do (when (or (= (mod i 3) 0) (= (mod i 5) 0)) (setq s (+ s i)))
      )
(print s)

---

program multiples;

var
    i: integer;
    s: longint;

begin
    s := 0;
    for i:=1 to 999 do
    begin
        if ((i mod 5)=0) or ((i mod 3)=0)
            then s := s+i;
    end;
    writeLn(s);
end.

