# 11 Attendance Tracking

## Goal
Implement a system to track student attendance for courses.

## Context
Students are enrolled in courses via the `enrollments` app. Attendance needs to be recorded per course session.

## Tasks
- [ ] Create `Attendance` model in the `students` or a new `attendance` app <!-- id: 6 -->
- [ ] Implement views for marking attendance <!-- id: 7 -->
- [ ] Add attendance report views (daily/monthly) <!-- id: 8 -->
- [ ] Update dashboard to show quick attendance stats <!-- id: 9 -->

## Sub-tasks (if any)
- [ ] Create migrations for the new model <!-- id: 10 -->
- [ ] Design the "Mark Attendance" UI using Studio Chalk theme <!-- id: 11 -->

## Verification
- [ ] Verify that attendance can be marked for an enrolled student <!-- id: 12 -->
- [ ] Run command `python manage.py test apps/students` <!-- id: 13 -->

When feature implemented successfully, move this file to `docs/completed/`.
