teks_ujian = input("Nilai ujian (0-100): ").strip()
teks_tugas = input("Nilai tugas (0-100): ").strip()
teks_hadir = input("Kehadiran persen (0-100): ").strip()

try:
    ujian = float(teks_ujian)
    tugas = float(teks_tugas)
    hadir = float(teks_hadir)

except ValueError:
    print("Masukan ditolak: seluruh data harus berupa angka.")

else:
    if not (0 <= ujian <= 100):
        print("Masukan ditolak: nilai ujian di luar rentang 0 sampai 100.")

    elif not (0 <= tugas <= 100):
        print("Masukan ditolak: nilai tugas di luar rentang 0 sampai 100.")

    elif not (0 <= hadir <= 100):
        print("Masukan ditolak: kehadiran di luar rentang 0 sampai 100.")

    else:
        akhir = 0.6 * ujian + 0.4 * tugas
        print(f"Nilai akhir = {akhir:.2f}")

        # 1. Periksa syarat kehadiran minimal 80%
        if hadir < 80:
            predikat = "D"
            status = "Belum Lulus"
            print("Kehadiran kurang dari 80%, sehingga belum memenuhi syarat lulus.")

        else:
            # 2. Tentukan predikat dengan rantai elif menurun
            if akhir >= 85:
                predikat = "A"
            elif akhir >= 75:
                predikat = "B"
            elif akhir >= 65:
                predikat = "C"
            else:
                predikat = "D"

            # 3. Tentukan status lulus atau belum lulus dari predikat
            if predikat == "A" or predikat == "B" or predikat == "C":
                status = "Lulus"
            else:
                status = "Belum Lulus"

        # 4. Tampilkan predikat dan status
        print(f"Predikat = {predikat}")
        print(f"Status = {status}")
